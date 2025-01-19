# Time Series Analysis Quiz

## Question 1 (1 point)
What is any behavior in time series data called if it is not described by long-term behavior, random low-frequency variations, or known periodicity?

**Options:**
1. Seasonal effect
2. Trend
3. Cycle
4. Residual

**Answer:** Option 4: Residual
- *Definition:* Residuals are the remaining variations in time series data after accounting for trend, seasonality, and cyclical components
- *Context:* They represent the random, irregular fluctuations that cannot be attributed to systematic patterns

## Question 2 (1 point)
To extract a trend from the time series data, a filter "f" is applied. Which components does it remove?

**Options:**
1. Seasonal
2. Residual
3. Part of a cycle
4. Part of a trend

**Answer:** Option 1: Seasonal
- *Definition:* Trend extraction filters primarily remove seasonal patterns and high-frequency variations
- *Context:* This allows the underlying long-term trend to be isolated by removing periodic/seasonal fluctuations

## Question 3 (1 point)
What happens if the residue is not stationary in a time series data?

**Options:**
1. The data exhibits stronger periodicity
2. The time series data becomes more predictable
3. The residuals become smaller in magnitude
4. It becomes difficult to model the time series accurately

**Answer:** Option 4: It becomes difficult to model the time series accurately
- *Definition:* Non-stationary residuals indicate underlying patterns or dependencies that haven't been properly accounted for
- *Context:* This violates key assumptions of many time series models, making predictions less reliable

## Question 4 (1 point)
How do you compute the time series prediction error?

**Options:**
1. Compute the mean squared difference between the predicted values and the actual values
2. Subtract the predicted values from the actual values and take the absolute value
3. Divide the predicted values by the actual values and take the absolute difference
4. Compute the mean absolute difference between the predicted values and the actual values

**Answer:** Option 1: Compute the mean squared difference between the predicted values and the actual values
- *Definition:* Mean Squared Error (MSE) is calculated as the average of squared differences between predictions and actual values
- *Context:* MSE is preferred as it penalizes larger errors more heavily and provides a differentiable metric

## Question 5 (1 point)
Which function in the statsmodels library is used to extract the trend from time series data given the "filter" and "data" as constructors?

**Options:**
1. convolution.filter(data,filter)
2. convolution_filter(data,filter)
3. convolution_filter(data)
4. convolution_filter(filter)

**Answer:** Option 2: convolution_filter(data,filter)
- *Definition:* The convolution_filter function applies a moving average filter to extract trends
- *Context:* It requires both the data array and the filter coefficients as parameters

---

# Answer Key
1. Option 4: Residual (Unexplained variations after accounting for systematic patterns)
2. Option 1: Seasonal (Primary component removed during trend extraction)
3. Option 4: Difficult to model accurately (Non-stationary residuals violate model assumptions)
4. Option 1: Mean squared difference (Standard metric for prediction error assessment)
5. Option 2: convolution_filter(data,filter) (Correct function signature for trend extraction)