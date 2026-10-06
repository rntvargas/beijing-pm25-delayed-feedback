# Exact executed methods, v0.3.0

This specification documents already executed exploratory analyses. It does not retroactively preregister them. The frozen code preserves the legacy machine key `ACI_delayed_projected`; the public method name is **ACI-inspired daily delayed-feedback heuristic (ADH)**. `CQR_adapted` means delay-specific quantile-model training, not hyperparameter selection for the quantile models. The delay-specific 15/31-leaf selection applies only to the point predictor.

## CQR

For each imposed delay d in {0,6,24,72,168} hours, reconstruct causal predictors. Fit separate histogram gradient boosting quantile regressors at .025, .05, .95, .975 using development responses with target_time + d strictly before 2015-03-01. Drop columns entirely missing in that training set only. All four models use 15 leaves, 100 iterations, learning rate .05, min_samples_leaf 40, l2_regularization 1, early_stopping False, random_state 20261003. Quantile/pinball loss is used, not the absolute-error point-model selection.

Clip each quantile prediction to nonnegative values, then sort the lower/upper pair pointwise. For alpha=.10 or .05, use models at alpha/2 and 1-alpha/2. Calibration includes naturally observed calibration responses with target_time strictly before 2016-02-23: n=101012 for all delays. This common cutoff ensures all included responses have arrived before the first test forecast at 2016-03-01 00:00, even at d=168 h.

Compute signed score s_i=max(lower_i-y_i,y_i-upper_i); do not take its absolute value or replace negative scores by zero. Let k=ceil((n+1)(1-alpha)), and take the k-th smallest score with no interpolation. The code asserts 1<=k<=n. The resulting correction q is positive in every executed configuration. It is fixed throughout the test period; no test responses update CQR. Output [max(0,lower-q),upper+q]. The code asserts q>=0; a dataset requiring a negative correction or k>n is outside this executed implementation and must trigger an explicit amendment, not silently use a different algorithm. Nonnegative truncation uses the nonnegative target support. No exchangeability or time-series coverage guarantee is asserted.

`verificar_cqr.py` independently sorts the scores, recomputes ranks/corrections from saved quantile models and checks every saved main-test endpoint. Results, crossing counts and latest permitted calibration arrivals are in `tables/cqr_algorithm_audit.csv`.

## ADH

This is a heuristic inspired by ACI, not a reproduction of unmodified ACI and not a new algorithm with a proved guarantee. For each nominal alpha, initialize a=alpha. At each daily midnight D, process first the responses of previously issued test forecasts whose arrival lies in (previous update,D]. Compute the equally weighted miscoverage rate of their actually issued intervals (boundaries count as covered). If at least one response arrived, set a=clip(a+0.01*(alpha-miss_rate),.001,.5); otherwise retain a. The first update has no test feedback. Each day receives one update regardless of the number of arriving responses; batches are not pooled by number of observations across days. Neither gamma nor projection limits were selected on the test.

Next use absolute point-model residuals whose arrivals lie in (D-30 days,D], pooling all stations, with the same finite-sample rank rule at 1-a. Issue [max(0,point_prediction-q),point_prediction+q] for all origins that day. Freeze the predictor. Arrival at exactly D is processed before issuance. The calibration and test residual pool, the rolling window, projection, daily batching and delayed feedback are explicit departures from original ACI theory. No original ACI guarantee is transferred to ADH.

## Paired exploratory uncertainty

`bootstrap_exploratorio.py` uses 10000 circular day-block draws at lengths 7,14,28 and seed 20261006+block_length. Whole days retain all stations. Each draw divides resampled sums of paired score differences by resampled observed-target counts, rather than averaging daily means equally. Intervals are pointwise percentile limits .025/.975, conditional on fixed fitted models and completed predictions. There is no refitting, multiplicity correction, or claim of exact validity under nonstationarity. Contrasts and seeds are specified in the executable script; main-period, earlier-period and heterogeneous-delay results have separate scenario labels. Negative differences favour the left method. The original primary bootstrap remains unchanged.

## Evidential status

- P: Original locally prespecified analysis, including its single primary contrast. Local timestamp/hash documentation is not public preregistration or independent confirmation.
- E: Comparators and paired uncertainty added after test inspection; exploratory.
- S: Block length, pooling, missingness, practical loss, heterogeneous delays and earlier-period checks; sensitivity analyses, with chronology retained. S includes both originally planned and post-review sensitivities; it is not an independent validation category.

No result in this package constitutes external independent confirmation. The historical protocol and legacy prediction files remain intact.
