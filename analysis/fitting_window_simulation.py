"""
Fitting-window simulation for:
  Mangrich et al. "Aperiodic neural dynamics as a transdiagnostic biomarker in
  Deep Brain Stimulation: a systematic review of spectral parameterization."

Quantifies how the estimated aperiodic exponent depends on the frequency window
used to fit it, across the 25 distinct primary windows used by the 27 included
reports that fitted a spectral model (manuscript Table: Aperiodic Fitting Range).

Reproduces Section 3.6.2 and Figure 5.

Requirements:  numpy, pandas, scipy, matplotlib, fooof==1.1.1
Runtime:       ~3 min on a laptop CPU.
"""
import numpy as np, pandas as pd, warnings
from fooof import FOOOF
from fooof.sim import gen_power_spectrum
from fooof.utils import interpolate_spectrum
warnings.filterwarnings("ignore")

CHI_TRUE = 1.5      # ground-truth aperiodic exponent
OFFSET   = 0.0
F_KNEE   = 17.0     # cortical knee frequency reported by Bush et al. (2024)
KNEE_P   = F_KNEE ** CHI_TRUE          # fooof knee parameter k = f_knee^chi
BETA_PK  = [20.0, 0.6, 4.0]            # centre (Hz), power, width
GEN_RANGE, FRES, NLV, NREP = (0.5, 400.0), 0.25, 0.005, 50
RNG = np.random.default_rng(20261103)  # seed used for the published result

# the 25 distinct primary fitting windows used by the corpus
WINDOWS = [(1,30),(1,36),(1,38),(1,50),(1,95),(1,100),(1,250),(2,45),(2,48),(2,49),
           (2,50),(2,60),(3,49),(3,70),(5,50),(5,70),(7,45),(8,50),(8,350),(10,50),
           (13,35),(20,45),(30,70),(30,100),(40,90)]

CONDS = {
    "no knee, no peak":   dict(ap=[OFFSET, CHI_TRUE],         pe=[]),
    "no knee, beta peak": dict(ap=[OFFSET, CHI_TRUE],         pe=BETA_PK),
    "knee, no peak":      dict(ap=[OFFSET, KNEE_P, CHI_TRUE], pe=[]),
    "knee, beta peak":    dict(ap=[OFFSET, KNEE_P, CHI_TRUE], pe=BETA_PK),
}

def fit_chi(freqs, powers):
    """Fit specparam in fixed (knee-free) mode, the mode used by most reports."""
    fm = FOOOF(peak_width_limits=(1, 12), max_n_peaks=6, min_peak_height=0.05,
               aperiodic_mode="fixed", verbose=False)
    fm.fit(freqs, powers)
    return fm.aperiodic_params_[-1], fm.r_squared_

def main():
    rows = []
    for cname, cfg in CONDS.items():
        for rep in range(NREP):
            np.random.seed(int(RNG.integers(0, 2**31 - 1)))
            fs, ps = gen_power_spectrum(GEN_RANGE, cfg["ap"], cfg["pe"],
                                        nlv=NLV, freq_res=FRES)
            for lo, hi in WINDOWS:
                m = (fs >= lo) & (fs <= hi)
                chi, r2 = fit_chi(fs[m], ps[m])
                rows.append(dict(cond=cname, rep=rep, lo=lo, hi=hi,
                                 win=f"{lo:g}-{hi:g}", chi=chi,
                                 err=chi - CHI_TRUE, r2=r2, special=""))
            # ID18 additionally excluded the 40-60 Hz line-noise band from its 1-95 Hz fit
            fi, pi = interpolate_spectrum(fs, ps, [40, 60])
            m = (fi >= 1) & (fi <= 95)
            chi, r2 = fit_chi(fi[m], pi[m])
            rows.append(dict(cond=cname, rep=rep, lo=1, hi=95,
                             win="1-95 (excl. 40-60)", chi=chi,
                             err=chi - CHI_TRUE, r2=r2, special="ID18"))

    df = pd.DataFrame(rows)
    df.to_csv("window_simulation_raw.csv", index=False)
    summ = (df.groupby(["cond", "win", "lo", "hi", "special"])
              .agg(chi_mean=("chi", "mean"), chi_sd=("chi", "std"),
                   err_mean=("err", "mean"), r2_mean=("r2", "mean"))
              .reset_index())
    summ.to_csv("window_simulation_summary.csv", index=False)

    prim = summ[summ.win != "1-95 (excl. 40-60)"]
    real = prim[prim.cond != "no knee, no peak"]
    print(f"ideal condition recovered chi in "
          f"[{prim[prim.cond=='no knee, no peak'].chi_mean.min():.3f}, "
          f"{prim[prim.cond=='no knee, no peak'].chi_mean.max():.3f}]")
    print(f"with knee and/or peak, chi ranged "
          f"{real.chi_mean.min():.2f} to {real.chi_mean.max():.2f}")
    big = prim[prim.err_mean.abs() > 0.5]
    print(f"{int((big.r2_mean>=0.95).sum())} of {len(big)} fits with |error|>0.5 "
          f"still reached R2 >= 0.95; min R2 = {prim.r2_mean.min():.3f}")

if __name__ == "__main__":
    main()
