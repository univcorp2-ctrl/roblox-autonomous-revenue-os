from __future__ import annotations

from dataclasses import dataclass

from .models import Metrics


@dataclass(frozen=True)
class RollbackVerdict:
    rollback: bool
    reason: str


def should_rollback(before: Metrics, after: Metrics) -> RollbackVerdict:
    if after.crash_rate > max(0.02, before.crash_rate * 1.5):
        return RollbackVerdict(True, "crash rate breached safety threshold")
    if before.d1_retention > 0 and after.d1_retention < before.d1_retention * 0.93:
        return RollbackVerdict(True, "D1 retention fell more than 7%")
    if before.revenue_usd_7d > 0 and after.revenue_usd_7d < before.revenue_usd_7d * 0.90:
        return RollbackVerdict(True, "7-day revenue fell more than 10%")
    return RollbackVerdict(False, "guardrails pass")
