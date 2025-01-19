# Mini-Lesson 10.1: Time Series Data

## Introduction
Time series data is a sequence of data points collected or recorded at successive points in time—often at uniform intervals. This type of data is typically used to analyze trends, cycles, or patterns over time. Time series data is essential in various fields such as finance, economics, environmental science, and engineering.

## Characteristics of Time Series Data
- **Temporal Order**: The data points are ordered in time, with each point corresponding to a specific time.
- **Regular Intervals**: Often, the data points are collected at regular intervals (e.g., daily, monthly, yearly).
- **Dependence on Time**: The value at any given time is often influenced by previous values.

## Types of Time Series Data
Time series data can be categorized based on various attributes and characteristics. Here are some common types of time series data:

### Based on Variables
- **Univariate Time Series**: A time series that consists of observations on a single variable recorded sequentially over time, e.g., daily closing prices of a single stock
- **Multivariate Time Series**: A time series that consists of observations on two or more variables recorded sequentially over time, e.g., daily records of temperature, humidity, and wind speed in a specific location

### Based on Time Intervals
- **Regular Time Series**: A time series where data points are collected at regular time intervals, e.g., monthly sales figures of a retail store
- **Irregular Time Series**: A time series where data points are collected at irregular time intervals, e.g., transaction timestamps in an online shopping system

### Based on Statistical Properties
- **Stationary Time Series**: A time series whose statistical properties such as mean, variance, and autocorrelation are constant over time, e.g., daily temperature deviations from the mean temperature in a climate-controlled environment
- **Non-Stationary Time Series**: A time series whose statistical properties change over time, e.g., the daily closing price of a stock, which can exhibit trends and changing variance

### Based on Patterns
- **Seasonal Time Series**: A time series that exhibits regular and predictable patterns that repeat over specific intervals, typically within a year, e.g., monthly ice cream sales, which increase during the summer months
- **Non-Seasonal Time Series**: A time series that does not exhibit regular and predictable patterns of seasonality, e.g., random daily fluctuations in stock prices without a seasonal component
- **Cyclic Time Series**: A time series that shows fluctuations with a period longer than a year, often related to business or economic cycles, e.g., multi-year business cycles showing periods of expansion and contraction

### Based on Predictability
- **Noisy Time Series**: A time series that contains a significant amount of randomness or noise, making it difficult to discern any clear patterns or trends, e.g., daily stock prices, which can have random fluctuations due to market volatility
- **Deterministic Time Series**: A time series where future values can be precisely determined by past values, often following a clear, predictable pattern, e.g., synthetic data generated from a known mathematical function
- **Stochastic Time Series**: A time series that is influenced by random variables and therefore inherently unpredictable, even if it follows some statistical properties, e.g., actual stock market prices, which are influenced by a multitude of unpredictable factors

## Python Support for Time Series Data
- **Pandas**: A powerful data manipulation and analysis library that supports time series data. It provides tools for handling time-stamped data, date ranges, and frequency conversion.
- **Statsmodels**: A library for statistical modeling and econometrics that includes tools for time series analysis, such as ARIMA, SARIMA, and state space models.
- **Scikit-Learn**: A machine learning library that includes tools for time series analysis and forecasting, although it is not specialized for time series data.
- **TensorFlow and Keras**: Libraries for building and training neural networks, including recurrent neural networks (RNNs) and long short-term memory networks (LSTMs) for time series forecasting.

## Different Time Series
Trends and seasonal patterns may be present in time series datasets. Trends can cause a change in the mean over time, while seasonality can change the variance over time, both of which define a time series as non-stationary. Conversely, you make assumptions about times series datasets that do not have these same trends or seasonality, and they are referred to as stationary.

### Stationary Time Series
A stationary time series of observations is not affected by time and has no trend or seasonal effects. Therefore, a stationary time series can be easier to model. Many statistical models assume or require a stationary time series.

### Non-Stationary Time Series
A non-stationary series of observations shows seasonal effects, trends, and other structures related to the time index. In the classic time series analysis and forecasting methods, trends are identified and removed from the data.

## Differencing Time Series Data
To transform a dataset into stationary data, it is critical to visualize it and determine the effects of non-stationary data. This can be accomplished by looking at a line plot of the series over time. A non-stationary series will show signs of apparent trends, seasonality, or other systematic structures.

Differencing can be deployed to transform a time series dataset by removing changes in the level of the time series, thereby eliminating structures such as trends and seasonality.
- Differencing is determined by computing the differences between consecutive observations (subtracting the previous observation from the current observation).