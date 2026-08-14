from revenueos import Experiment, Metrics, choose, should_rollback


def base_metrics(**overrides):
    data = dict(dau=1000, payer_conversion=0.01, arp_dau=0.03, d1_retention=0.20, revenue_usd_7d=200.0, crash_rate=0.001)
    data.update(overrides)
    return Metrics(**data)


def test_spend_is_never_fully_autonomous():
    decision = choose(base_metrics(), [Experiment("ads", 0.2, 0.0, 0.1, 0.1, requires_spend=True)])
    assert decision.action == "human_gate"


def test_pricing_starts_as_canary():
    decision = choose(base_metrics(), [Experiment("price", 0.2, 0.0, 0.1, 0.1, touches_pricing=True)])
    assert decision.action == "canary"


def test_crash_guardrail_halts_changes():
    decision = choose(base_metrics(crash_rate=0.03), [Experiment("ui", 0.1, 0.1, 0.1, 0.1)])
    assert decision.action == "hold"


def test_revenue_regression_rolls_back():
    verdict = should_rollback(base_metrics(revenue_usd_7d=200), base_metrics(revenue_usd_7d=150))
    assert verdict.rollback is True
