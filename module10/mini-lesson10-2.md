# Mini-Lesson 10.2: Statsmodel

Statsmodels offers a rich set of tools for time series analysis and forecasting, covering a wide range of models and diagnostic tests. It provides robust implementations of classical time series models, such as ARIMA and SARIMA, as well as more advanced models, such as state space models and VAR. This makes statsmodels a valuable resource for anyone working with time series data in Python.

## Time Series Analysis (TSA)

`statsmodels.tsa` contains model classes and functions that are useful for time series analysis. Basic models include univariate autoregressive models (AR), vector autoregressive models (VAR), and univariate autoregressive moving average models (ARMA). Non-linear models include Markov switching dynamic regression and autoregression. It also includes descriptive statistics for time series, e.g., autocorrelation, partial autocorrelation function, and periodogram, as well as the corresponding theoretical properties of ARMA or related processes. It also includes methods to work with autoregressive and moving average lag-polynomials.

The module structure is within `statsmodels.tsa`:

- **stattools**: Empirical properties and tests, ACF, PACF, Granger causality, ADF unit root test, KPSS test, BDS TEST, Ljung–Box test, and others.
- **ar_model**: Univariate autoregressive process, estimation with conditional and exact maximum likelihood and conditional least squares.
- **model**: Univariate ARIMA process and estimation with alternative methods.
- **statespace**: Comprehensive statespace model specification and estimation. See the statespace documentation.
- **vector_ar, var**: Vector autoregressive process (VAR) and vector error correction models, estimation, impulse response analysis, forecast error variance decompositions, and data visualization tools. See the vector_ar documentation.
- **arma_process**: Properties of ARMA processes with given parameters, including tools to convert between ARMA, MA, and AR representation as well as ACF, PACF, spectral density, and impulse response function.
- **tsa.fftarma**: Similar to arma_process but working in the frequency domain.
- **tsatools**: Additional helper functions to create arrays of lagged variables, construct regressors for trend, detrend, and similar.
- **filters**: Helper function for filtering time series.
- **regime_switching**: Markov switching dynamic regression and autoregression models

The main estimation classes, which can be accessed through `statsmodels.tsa.api`, are as follows:

- Univariate autoregressive processes
- Autoregressive moving-average processes (ARMA) and Kalman filter
- Exponential smoothing
- ARMA process
- Autoregressive distributed lag models
- Error correction models
- Vector autoregressions