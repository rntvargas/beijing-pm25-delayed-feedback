# Beijing PM2.5: delayed measurements and delayed feedback

Research benchmark by **Renato Quispe Vargas**, Universidad Nacional del Altiplano.

**Status: exploratory research manuscript under author review, not an accepted article.**
No new conformal algorithm or distribution-free guarantee is claimed. Funding, competing interests, CRediT contributions and correspondence details await author confirmation.

## What is evaluated

Hourly UCI Beijing multi-site data, 12 stations, 2013–2017; 24-hour forecasts; simulated PM2.5 delays of 0, 6, 24, 72 and 168 hours. Other measured channels remain available with their natural missingness. A station-heterogeneous delay sensitivity is also included. These are synthetic delivery scenarios, not measured network latencies.

The initial fixed-predictor comparison is preserved. A separately documented **post-review exploratory extension** adds:
- delay-adapted model selection and training with arrival-purged responses;
- raw conditional quantile intervals and conformalized quantile regression (CQR);
- daily delayed-feedback projected ACI (explicit batching/projection modifications; no original-ACI theorem claimed);
- pooled, station-specific and equal-station-weight calibration;
- coverage and paired-difference block-bootstrap intervals, subgroup simultaneous bands;
- missingness, concentration strata, score distributions and hypothetical loss sensitivity;
- a second, earlier Beijing temporal backtest, not independent external validation;
- arrival ledgers and independent numerical verification in R.

At 72 hours and 90% nominal level, original rolling calibration has coverage 88.32% and interval score 328.01. Exploratory CQR has coverage 88.91% and score 258.40; projected delayed ACI has coverage 89.78% and score 317.48. The additional comparisons use a previously examined test set and are not confirmatory. No uniform superiority or deployment suitability is established.

Repository: https://github.com/rntvargas/beijing-pm25-delayed-feedback

Full research release: https://github.com/rntvargas/beijing-pm25-delayed-feedback/releases/tag/v0.2.0

## Files and reproducibility

`source_and_tables.zip` contains the complete directory-preserving source, manuscript and result tables. Extract it into an empty project directory. The accompanying full reproducibility release includes the original data, prepared partitions, fitted models, all predictions and timing ledgers. Each archive includes SHA256 checksums. The source archive is sufficient to regenerate the results after downloading/preparing the data.

Python 3.12.14; R 4.5.2. From the extracted project root:

```text
python -m pip install -r outputs/03_experimento/requirements.txt
python download_data.py
python outputs/02_datos_estudio/preparar_datos.py
python outputs/03_experimento/experimento.py --stage development
python outputs/03_experimento/experimento.py --stage final
python outputs/05_revision/revision.py
python outputs/05_revision/segundo_periodo.py
python outputs/05_revision/diagnosticos.py
python outputs/05_revision/verificar_tiempos.py
Rscript outputs/05_revision/verificar_revision.R outputs/05_revision
tectonic outputs/04_manuscrito_springer/manuscript.tex
```

`revision.py` resumes completed delay files. To conduct a clean rerun, use a fresh extraction and avoid mixing result versions. The older model experiment overwrites its own outputs when rerun. The manuscript source is editorially maintained; the original figure generator does not overwrite it.

The notebook-style or GUI use of RStudio/VS Code is optional. Calculations run from scripts; QGIS was not needed for this non-cartographic experiment. Serialized joblib models should only be loaded from trusted copies of this package.

## Data, licensing and attribution

Data: Chen (2017), Beijing Multi-Site Air Quality, UCI Machine Learning Repository, DOI https://doi.org/10.24432/C5RK5G, **CC BY 4.0**. Original ZIP SHA256: `b04da438b2f331ac0ffd45aebdfec0d20d2367feb5f6948c4b1f7ce1191e33c4`.

Original analysis code: MIT (see LICENSE). Data retain CC BY 4.0. Springer template files retain their original notices; the MIT license does not relicense those files or cited publications. Manuscript and generated figures remain research materials under author review; no journal acceptance is implied.

## Verification and limitations

R independently reproduced all 68 extension interval-summary rows within 1e-8. Timing checks independently reproduced 90 daily quantiles, checked all residual event ledgers and verified invariance to perturbing unavailable responses. These checks establish implementation consistency, not correctness of every scientific assumption.

Intervals are evaluated only for naturally observed targets. No missing-at-random mechanism is established; no population correction is claimed. Bootstrap inference conditions on fitted models and is sensitive to block size and nonstationarity. The data cover one city; the earlier temporal sensitivity overlaps the study history. Public archiving with a persistent DOI remains pending: **a GitHub URL is not a DOI**.

## AI assistance

OpenAI Codex assisted with searches, design, programming, execution, checking and drafting. Renato Quispe Vargas must review and approve the scientific content before submission; that approval is not asserted by publishing this research package. AI is not an author.
