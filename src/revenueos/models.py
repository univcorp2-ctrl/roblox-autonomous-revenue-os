from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Metrics:
    dau: int
    payer_conversion: float
    arp_dau: float
    d1_retention: float
    revenue_usd_7d: float
    crash_rate: float = 0.0


@dataclass(frozen=True)
class Experiment:
    name: str
    expected_conversion_lift: float
    expected_retention_lift: float
    implementation_cost: float
    blast_radius: float
    requires_spend: bool = False
    touches_pricing: bool = False


@dataclass(frozen=True)
class Decision:
    experiment: str
    score: float
    action: str
    reason: str
