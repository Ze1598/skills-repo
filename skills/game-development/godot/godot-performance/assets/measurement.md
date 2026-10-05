# Capture, compare and report

## Representative cases

Select a few cases that exercise the complaint: stationary view; camera turns; movement through dense content; doors or group boundaries; a busy interaction; and repeated reset if memory growth is involved. Keep start state, camera, movement, input, content counts and duration reproducible. Include the actual maximized/fullscreen drawable if that is where the issue occurs.

Separate first-use stalls from warmed steady-state samples. Label shader/resource preparation, loading and gameplay distinctly; do not delete inconvenient gameplay spikes. Repeat noisy results before attributing a change. A short sample cannot establish long-session stability or heat reduction.

## Timing discipline

Record what the number actually measures: CPU callback duration, physics time, GPU time, engine frame interval, externally observed presentation, or explicit render submission/synchronization. CPU and GPU can overlap; do not add them as if strictly serial. An interval sampled from callbacks is not direct presentation evidence.

Keep screenshots and GPU readback outside timed intervals. Ensure native drawing is happening: headless execution cannot prove GPU performance, and background windows may stop drawing or throttle. If explicit drawing/synchronization is required, document its cost and keep that method identical across comparisons. Monitor counter scope: one viewport's draws differ from all-view draws.

Record frame limits, VSync and focus/menu throttling. A cap-limited mean is not unlimited throughput. Temporary uncapped testing can diagnose throughput, but restore the production policy and also test its pacing. Inspect median, p95, p99, worst interval and over-budget counts. Record the number and duration of samples; interpret sparse percentiles cautiously.

## Bundled analyzer

Run the bundled `frame_report.py` with Python 3 and an explicit `--budget-ms` value. It uses the standard library. Input CSV requires `scenario`, `phase` and `frame_ms` columns; phases are `warmup` or `measure`. Additional columns are ignored. Intervals must be finite and positive. Warmup rows are counted but excluded from distributions.

For example, from this skill's root:

```sh
python3 assets/frame_report.py capture.csv --budget-ms 16.666667 --metadata capture.json --output report.json
```

The CSV and metadata are new artifacts from the current task, not files shipped by or referenced from another project. The metadata JSON should contain these keys: `engine_version`, `build`, `hardware`, `renderer`, `driver`, `window_mode`, `output_size`, `render_size`, `frame_cap`, `vsync`, `timing_method`. Sizes are physical pixel dimensions; use frame_cap 0 for uncapped. Add scenario setup and cold/warm notes as useful. Missing metadata produces explicit limitations, not fabricated defaults.

The script uses nearest-rank percentiles and counts intervals strictly greater than the supplied budget. It analyzes each scenario separately and never converts a render-sync interval into a claim of presented FPS. It refuses malformed or empty measurement data.

## Compare before reporting

Review metadata before comparing reports. Changed resolution, content, sampling method, build mode, VSync or hardware can invalidate a causal comparison. State intentional changes, such as a renderer replacement, and keep other conditions constant. If resolution was also changed, provide a same-resolution run to separate the effects.

Report: symptom and reproduction; suspected bottleneck and evidence; intervention and visible tradeoffs; comparable before/after timings and counters; correctness checks; remaining limitations. Label a result inconclusive if noise or the timing method cannot support the claim.

Primary source: [Godot general optimization](https://docs.godotengine.org/en/stable/tutorials/performance/general_optimization.html).
