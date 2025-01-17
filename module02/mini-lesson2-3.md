# Mini-Lesson 2.3: Outliers and Quartiles

## Introduction to Outliers

Outliers are data points that significantly differ from other data points in a dataset. These observations are rare or distinct and can skew statistical analysis, leading to misleading results. Outliers can occur due to various reasons, such as:
- Measurement errors
- Experimental variability
- Natural variation in the data

Identifying and handling outliers is important in data analysis for ensuring the accuracy and reliability of statistical models. This is the most important step in data preprocessing. Removing outliers in data preprocessing is essential for ensuring the accuracy, reliability, and validity of data analysis and ML models.

## Methods for Identifying Outliers

### 1. Visual Inspection
Outliers can be visualized using plots such as:
- Histograms
- Scatter plots
- Box plots

The outlier points appear far away from the bulk of data.

### 2. Statistical Methods

#### Z-Score
The Z-score measures how many standard deviations an observation is from the mean. Data points with a Z-score above a certain threshold (e.g., 3) are considered outliers.

#### Interquartile Range (IQR)
Calculate the IQR, which is the difference between the 75th and 25th percentiles of the data. Data points that fall below Q1 − 1.5 × IQR or above Q3 + 1.5 × IQR are considered outliers, where Q1 and Q3 are the 25th and 75th percentiles, respectively.

### 3. Clustering
Clustering algorithms can be used to group similar data points together. Data points that do not belong to any cluster or are in a cluster by themselves can be considered outliers.

## Z-Score Details

The Z-score, also known as the standard score, is a statistical measure that quantifies the number of standard deviations a data point is from the mean of the dataset.

### Formula
```
Z = (X - μ) / σ
```

Where:
- Z is the Z-score of the data point
- X is the value of the data point
- μ is the mean of the dataset
- σ is the standard deviation of the dataset

The Z-score value helps to identify outliers. Data points with Z-scores greater than a certain threshold (e.g., 3) are considered outliers, as they are significantly far from the mean and may represent unusual or erroneous data.

## Inter Quartile Range (IQR)

The interquartile range (IQR) is a measure of statistical dispersion, or spread, that is calculated as the difference between the 75th percentile (Q3) and the 25th percentile (Q1) of a dataset. In other words, IQR represents the range of the middle 50% of the data.

### Formula
```
IQR = Q3 - Q1
```

Where:
- Q1 is the 25th percentile (the value below which 25% of the data falls)
- Q3 is the 75th percentile (the value below which 75% of the data falls)

The IQR is a robust measure of spread, meaning that it is not influenced by extreme values or outliers in the dataset. It is often used in conjunction with box plots to visually identify outliers in a dataset.