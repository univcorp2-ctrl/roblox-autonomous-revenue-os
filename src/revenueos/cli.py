from __future__ import annotations

import argparse
import json

from .decision import choose
from .models import Experiment, Metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="Choose the next autonomous Roblox revenue experiment")
    parser.add_argument("input", help="Path to JSON containing metrics and experiments")
    args = parser.parse_args()
    payload = json.load(open(args.input, encoding="utf-8"))
    metrics = Metrics(**payload["metrics"])
    experiments = [Experiment(**item) for item in payload["experiments"]]
    decision = choose(metrics, experiments)
    print(json.dumps(decision.__dict__, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
