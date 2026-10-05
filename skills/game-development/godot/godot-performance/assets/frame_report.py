#!/usr/bin/env python3
"""Summarize measured frame intervals without claiming presented FPS."""
import argparse
import csv
import json
import math
from pathlib import Path
import sys

META_KEYS = (
    "engine_version", "build", "hardware", "renderer", "driver", "window_mode",
    "output_size", "render_size", "frame_cap", "vsync", "timing_method",
)


def percentile(values, fraction):
    """Nearest rank, on sorted nonempty values."""
    return values[max(0, math.ceil(len(values) * fraction) - 1)]


def analyze(capture, budget_ms, metadata=None):
    if not math.isfinite(budget_ms) or budget_ms <= 0:
        raise ValueError("budget_ms must be finite and positive")
    if metadata is not None and not isinstance(metadata, dict):
        raise ValueError("metadata must be a JSON object")
    groups = {}
    warmup_rows = 0
    with Path(capture).open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        headers = reader.fieldnames or []
        if len(set(headers)) != len(headers):
            raise ValueError("duplicate CSV column names")
        if not {"scenario", "phase", "frame_ms"}.issubset(headers):
            raise ValueError("CSV requires scenario, phase and frame_ms columns")
        for row in reader:
            line = reader.line_num
            if None in row or any(row.get(k) is None for k in ("scenario", "phase", "frame_ms")):
                raise ValueError(f"line {line}: malformed CSV row")
            scenario = row["scenario"].strip()
            phase = row["phase"].strip()
            if not scenario or phase not in ("warmup", "measure"):
                raise ValueError(f"line {line}: scenario must be nonempty; phase must be warmup or measure")
            try:
                value = float(row["frame_ms"])
            except ValueError as exc:
                raise ValueError(f"line {line}: invalid frame_ms") from exc
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f"line {line}: frame_ms must be finite and positive")
            if phase == "warmup":
                warmup_rows += 1
            else:
                groups.setdefault(scenario, []).append(value)
    if not groups:
        raise ValueError("capture contains no measured intervals")
    meta = metadata if metadata is not None else {}
    missing = [key for key in META_KEYS if key not in meta or meta[key] is None or meta[key] == ""]
    warnings = ["Intervals retain the capture's timing semantics; this report does not establish presented FPS."]
    if missing:
        warnings.append("Comparison metadata missing: " + ", ".join(missing))
    scenarios = {}
    for name, intervals in sorted(groups.items()):
        values = sorted(intervals)
        count = len(values)
        over = sum(value > budget_ms for value in values)
        scenarios[name] = {
            "samples": count,
            "sum_interval_ms": math.fsum(values),
            "mean_ms": math.fsum(values) / count,
            "p50_ms": percentile(values, 0.50),
            "p95_ms": percentile(values, 0.95),
            "p99_ms": percentile(values, 0.99),
            "min_ms": values[0],
            "max_ms": values[-1],
            "intervals_over_budget": over,
            "percent_over_budget": over * 100.0 / count,
        }
        if count < 300:
            warnings.append(f"{name}: only {count} intervals; upper percentiles are sparse.")
    return {
        "schema_version": 1,
        "budget_ms": budget_ms,
        "percentile_method": "nearest_rank",
        "excluded_warmup_rows": warmup_rows,
        "metadata": meta,
        "scenarios": scenarios,
        "limitations": warnings,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("capture", type=Path, help="CSV with scenario, phase, frame_ms")
    parser.add_argument("--budget-ms", required=True, type=float)
    parser.add_argument("--metadata", type=Path, help="JSON capture conditions")
    parser.add_argument("--output", type=Path, help="write JSON report instead of stdout")
    args = parser.parse_args()
    try:
        inputs = {args.capture.resolve()}
        if args.metadata:
            inputs.add(args.metadata.resolve())
        if args.output and args.output.resolve() in inputs:
            raise ValueError("output must not overwrite a capture or metadata input")
        metadata = json.loads(args.metadata.read_text(encoding="utf-8")) if args.metadata else None
        report = analyze(args.capture, args.budget_ms, metadata)
        body = json.dumps(report, indent=2, allow_nan=False) + "\n"
        if args.output:
            args.output.write_text(body, encoding="utf-8")
        else:
            sys.stdout.write(body)
    except (OSError, ValueError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
