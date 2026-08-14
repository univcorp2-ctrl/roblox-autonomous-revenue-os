from __future__ import annotations

from .models import Decision, Experiment, Metrics


def score_experiment(metrics: Metrics, experiment: Experiment) -> float:
    """Rank work by expected revenue leverage per unit of implementation risk."""
    monetization_headroom = max(0.0, 0.05 - metrics.payer_conversion) / 0.05
    retention_headroom = max(0.0, 0.35 - metrics.d1_retention) / 0.35
    opportunity = (
        experiment.expected_conversion_lift * (1.0 + monetization_headroom)
        + experiment.expected_retention_lift * (0.7 + retention_headroom)
    )
    risk = 1.0 + max(0.0, experiment.implementation_cost) + 2.0 * max(0.0, experiment.blast_radius)
    return opportunity / risk


def choose(metrics: Metrics, experiments: list[Experiment]) -> Decision:
    if not experiments:
        return Decision("none", 0.0, "hold", "no experiments proposed")

    ranked = sorted(
        ((score_experiment(metrics, item), item) for item in experiments),
        key=lambda pair: pair[0],
        reverse=True,
    )
    score, best = ranked[0]

    if metrics.crash_rate > 0.02:
        return Decision(best.name, score, "hold", "crash-rate guardrail active")
    if best.requires_spend:
        return Decision(best.name, score, "human_gate", "external spend is never autonomous")
    if best.touches_pricing:
        return Decision(best.name, score, "canary", "pricing changes start as a canary")
    if score <= 0:
        return Decision(best.name, score, "hold", "no positive expected value")
    return Decision(best.name, score, "execute", "highest eligible expected revenue leverage")
