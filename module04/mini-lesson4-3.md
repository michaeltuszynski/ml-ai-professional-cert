# Mini-Lesson 4.3: Steps to Data Cleaning

Cleaning data means properly fixing, removing, or correcting data that may be incorrect, corrupted, incorrectly formatted, duplicated, or incomplete. The steps in the data cleaning process will vary from dataset to dataset, so there is no one method that prescribes the exact steps. Still, it is critical to establish a framework to cover some basic best practices.

## Step 1: Eliminate Duplicates
The duplication of data can happen during data collection and cause many problems in your dataset. Therefore, you must create a process to monitor and remove any duplicate data.

Pandas has a `duplicated()` method to identify duplicate rows in a DataFrame. This method returns a Boolean series indicating whether each row is a duplicate of a previous row. This series can be used to filter out duplicate rows or count the number of duplicates.

## Step 2: Resolve Structural Errors
You may discover structural errors during data integration. These errors are often tied to incorrect capitalization, naming conventions, and typos. In addition, due to inconsistencies, categories and classes may be mislabeled. For example, both N/A and "not applicable" can appear, but they must be analyzed as one category.

Incorrect data types in a dataset can be fixed by converting them to the correct data types. First, the columns are identified using the `dtype` attribute of the DataFrame. Then, the `astype()` method is used to convert columns to the correct data types. The errors during conversions are handled by using the `errors` parameter. The errors are converted into NaN entries.

## Step 3: Filter Outliers
It is common to find one-off observations that, at first glance, do not seem to fit within the data you are analyzing. The performance of the data will often benefit from removing these one-off outliers, such as an incorrect data entry. However, just because an outlier exists does not mean it is inaccurate. To determine whether it is accurate, you must validate its correctness before removing it.

Validating the correctness of outliers involves assessing whether the identified outliers are genuine data points that represent true extreme values or if they are errors or anomalies in the data. Some common methods used for validating outliers are as follows:

- **Domain knowledge**: Use domain knowledge to determine if the values identified as outliers are plausible given the context of the data. For example, if the dataset contains information about human heights and a value of 300cm (10 feet) is identified as an outlier, it could be an error in data entry.
- **Visual inspection**: Plot the data and visually inspect the distribution to identify outliers. Box plots, histograms, and scatterplots are commonly used for this purpose. Outliers will often be visually distinct from the rest of the data points.
- **Statistical methods**: Use statistical methods to identify outliers, such as Z-scores or interquartile range (IQR). Data points that fall outside a certain range (e.g., more than three standard deviations from the mean or outside 1.5 times the IQR) can be flagged as outliers.
- **Consultation**: Consult with subject-matter experts or other stakeholders to validate outliers, especially in complex or domain-specific datasets where the significance of outliers may not be immediately apparent.

## Step 4: Handle Missing Data
You cannot ignore missing data because many algorithms will not process missing values. However, several approaches exist to deal with them. For example, if you have null values, you can replace them with NULL or N/A if they have no impact on your analysis.

Missing values are the values that are not present in a dataset but are expected to be there. They can occur for various reasons, such as data entry errors, equipment malfunction, or simply because the information was not collected.

Identifying missing values:
- Check for null values using the `isnull()` function in the DataFrame.
- Count the number of missing values by using the `sum()` method on the result of `isnull()`.
- If the missing values are less, use `dropna()` method to drop those rows and columns.
- If the missing values are more, then the `fillna()` method is used to fill the missing values. The missing values can be filled using the `mean()`, `median()`, `mode()` method.

## Step 5: Validate
As a final step in the process, you should be able to validate that the data meets your project's requirements. At this point, you should have the ability to run descriptive statistics on the data to ensure that your dataset meets established best practices. You should also consider visualizing the data to determine any additional insights that might impact your project before proceeding.

During data preprocessing, several descriptive statistics are commonly used to understand the characteristics of the data. These statistics provide insights into the distribution, central tendency, and variability of the data. Some of the key descriptive statistics used in data preprocessing include:

- **Mean**: The average value of the data, calculated as the sum of all values divided by the number of values. Using NumPy, `mean()` is used for calculating the mean.
- **Median**: The middle value of the data when it is sorted in ascending or descending order. It is less affected by outliers than the mean. `median()` is used for calculating the median.
- **Mode**: The most frequently occurring value in the data. It can also be used for categorical data.
- **Standard deviation**: A measure of the dispersion of the data points around the mean. It indicates how spread out the values are from the average. `std()` is used for calculating the standard deviation.
- **Variance**: The average of the squared differences from the mean. It quantifies the spread of the data. `np.var()` is used for calculating the variance.
- **Range**: The difference between the maximum and minimum values in the data. It provides a measure of the spread of the data.
- **Percentiles**: Values that divide the data into 100 equal parts. For example, the 25th percentile (also known as the first quartile) is the value below which 25% of the data falls. `np.percentile()` is used for computing the percentiles.
- **Skewness**: A measure of the asymmetry of the distribution of the data. Positive skewness indicates a tail to the right, while negative skewness indicates a tail to the left. Use `stats.skew()` to calculate the skewness of an array.
- **Kurtosis**: A measure of the peak for the distribution of the data. Higher kurtosis indicates a sharper peak around the mean. Use `scipy.stats.kurtosis()` to calculate the kurtosis of an array.