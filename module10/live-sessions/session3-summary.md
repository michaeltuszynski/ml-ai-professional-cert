# Module 10 - Live Session 3 Summary

## Topic: Time Series Analysis and ARIMA Models

### Key Topics Covered

1. **Time Series Components**
   - Trend identification
   - Seasonality patterns
   - Moving averages (7-day, 14-day)
   - Limitations of time series forecasting

2. **ARIMA Model Components**
   - AR (Auto Regression)
   - I (Integrated)
   - MA (Moving Average)
   - Parameters: p, d, q

3. **Parameter Selection**
   - P: Order of auto regression (number of lags)
   - D: Degree of differencing (normalization)
   - Q: Order of moving average (error terms)
   - S: Seasonal component (for SARIMA)

### Important Concepts

1. **Auto Regression (AR)**
   - Uses lag plots
   - Can have decimal values for lags
   - Typically uses positive notation (t+1) though looking at past values

2. **Moving Averages**
   - Simple moving average
   - Exponential weighted
   - Weighted moving average

3. **Model Evaluation**
   - AIC (Akaike Information Criterion) as primary loss function
   - Importance of splitting data for validation
   - Not using entire dataset for forecasting

### Best Practices

1. **Data Splitting**
   - Don't use entire dataset for forecasting
   - Keep portion for validation
   - Ensure sufficient seasonal cycles in training data

2. **Parameter Selection**
   - Use ACF and PACF plots to determine parameters
   - Start with d=0 for differencing
   - Iterate through parameter combinations to find optimal AIC

3. **Forecasting Guidelines**
   - Short-term forecasting more reliable than long-term
   - Consider data frequency when determining forecast horizon
   - Account for external factors not captured in time series

### Additional Topics

1. **Seasonal Decomposition**
   - Using seasonal_decompose function
   - Identifying trend components
   - Extracting seasonal patterns

2. **ANOVA Regression**
   - Brief introduction to categorical variable regression
   - Use cases in A/B testing and categorical analysis

### Tools and Functions

1. **Stats Models Library**
   - ARIMA implementation
   - Seasonal decomposition
   - ACF and PACF plotting

2. **Parameter Optimization**
   - Functions for iterating through parameter combinations
   - AIC calculation and comparison
   - Model validation techniques