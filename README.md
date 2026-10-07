# Beijing PM2.5 delayed-feedback benchmark

Renato Quispe Vargas, Universidad Nacional del Altiplano. Correspondence: rntvargasvav@gmail.com.

Research revision **v0.4.0**: https://github.com/rntvargas/beijing-pm25-delayed-feedback/releases/tag/v0.4.0

The 28-page Springer-format manuscript contains 31 DOI-linked references. It is an exploratory research manuscript, not a submitted or accepted article. The author confirmed review of the preceding version, no funding and no competing interests. The new factorial and sensitivity results require author review before submission.

## What changed

- A 2 x 3 predictor/calibrator factorial across five delays and two nominal levels: 60 configurations, using saved fixed and delay-adapted predictors with static delay-matched calibration, rolling global calibration and ADH. No refitting or selection on test results.
- 270 paired score-contrast rows from 10000 circular day-block replicates at 7/14/28 days; within-predictor, within-calibrator and interaction contrasts. Pointwise, conditional-on-fit, no multiplicity adjustment.
- 40 random balanced station-delay assignments (three stations each at 6/24/72/168 h), with mappings and assignment dispersion.
- Exact coverage counts/disagreement sets and calibration/test distribution diagnostics.
- Local protocol recorded before execution replaces claims of local prespecification; detailed AI use restored; verification counts and cross-references clarified; DOI display repaired.

At 72 h and 90% nominal, scores for fixed/adapted predictors are 375.39/346.75 under static delay-matched calibration, 328.01/312.66 under rolling, and 317.48/303.20 under ADH. Adapting the predictor under rolling changes score by -15.35, with a 14-day pointwise interval [-24.67,-6.55]. Interaction intervals include zero. CQR remains a whole-pipeline comparator; this factorial does not identify all its component effects.

Global, station-specific and equal-station rolling each cover exactly 90493 of 102465 targets at 72 h/90%. Their membership differs: station pooling gains and loses 1048 cases, equal weighting gains and loses three. Equal marginal counts are not identical predictions.

## Reproducibility

Download `source_and_tables.zip` from this repository or the full research ZIP from the release. Extract to an empty project directory. The source archive excludes data, fitted models, prediction files and cached arrays; the full archive includes them. Both contain SHA256 manifests.

Existing scientific scripts, models and numerical results remain unchanged. Additional work is under `outputs/06_factorial`. Python 3.12.14 and R 4.5.2 were used. To regenerate everything from the source archive, first run the original preparation/analysis in order:

```text
python -m pip install -r outputs/06_factorial/requirements.txt
python download_data.py
python outputs/02_datos_estudio/preparar_datos.py
python outputs/03_experimento/experimento.py --stage development
python outputs/03_experimento/experimento.py --stage final
python outputs/05_revision/revision.py
python outputs/05_revision/segundo_periodo.py
python outputs/05_revision/diagnosticos.py
python outputs/05_revision/bootstrap_exploratorio.py
python outputs/05_revision/verificar_cqr.py
python outputs/05_revision/auditar_muestra_cqr.py
python outputs/05_revision/verificar_tiempos.py
Rscript outputs/05_revision/verificar_revision.R outputs/05_revision
python outputs/06_factorial/factorial.py
Rscript outputs/06_factorial/verify_factorial.R outputs/06_factorial
python outputs/06_factorial/plot_distributions.py
tectonic outputs/04_manuscrito_springer/manuscript.tex
```

With the full archive, the stored models are sufficient to run the last three analysis commands without refitting. For a clean verification of cached point predictions, use a fresh source extraction; `factorial.py` reuses its own completed cache if present. The manuscript is editorially maintained. Only load serialized models from trusted copies.

R recomputed all 60 new metric rows and covered counts (maximum discrepancy <3e-13). All 30 fixed cells reproduce saved interval bounds. The optimized loop matches the previous implementation for 16 heterogeneous method/level/assignment combinations. The alphabetical-assignment metrics match the previous saved results. See `QA_MANIFEST.json` and the supplementary tables.

## Archives, attribution and limits

Data: UCI Beijing Multi-Site Air Quality, https://doi.org/10.24432/C5RK5G (CC BY 4.0). Original analysis code: MIT. Springer files retain their notices; MIT does not relicense the manuscript, data or cited publications.

Frozen code DOI: https://doi.org/10.5281/zenodo.23171630 identifies **software v0.3.0 only**. It does not contain the v0.4.0 factorial extension, data, models, predictions or manuscript. `CITATION.cff` continues to describe that frozen code snapshot; cite the v0.4.0 GitHub release separately when using the new extension. No article DOI is claimed.

The test set was previously inspected; all additions are exploratory. The earlier Beijing backtest is not independent external validation. Simulated delays, temporal dependence, missing targets, one city and sensitivity to block length limit generalization. No new algorithm, universal coverage guarantee or Q1 acceptance is claimed.

## AI assistance

OpenAI Codex desktop (recorded model gpt-6-astra) assisted during 2–7 October 2026 with literature discovery, design, programming, computational execution and checking, plots and drafting. Computational checks are not independent human reproduction. The author confirmed review and responsibility for the preceding version; the new results need renewed review. See the detailed manuscript declaration and `RESPUESTA_REVISION_V040.md`.
