# analysis/

Fitting-window simulation reported in Section 3.6.2 and Figure 5 of the manuscript.

| File | Contents |
|------|----------|
| `fitting_window_simulation.py` | Simulation and fitting code (fooof 1.1.1) |
| `window_simulation_summary.csv` | Mean, SD, error and R² per window × condition (104 rows) |
| `window_simulation_raw.csv` | All 5,200 individual fits |
| `figure5_window_simulation.pdf` | Figure 5 as published |

## What it shows

A simulated source of known exponent (χ = 1.5) was fitted over each of the 25
distinct primary windows used by the included reports, in four generative
conditions crossing the presence of a 17 Hz knee with a 20 Hz beta peak,
50 noise realizations each.

- On an ideal power law every window recovered χ = 1.50 (max error 0.002).
- With a knee and/or a periodic peak, the same source was recovered as anything
  between **0.32 and 3.16**.
- Window choice exceeded estimation noise by at least a factor of 40.
- Goodness of fit did not detect the bias: 38 of the 41 window × condition
  combinations with |error| > 0.5 still reached R² ≥ 0.95 (minimum R² 0.899).

## Reproducing

```bash
pip install numpy pandas scipy matplotlib fooof==1.1.1
python fitting_window_simulation.py
```

The random seed is fixed, so the published values are reproduced exactly.
