# Module 9 Quiz

## Question 1 (1 pt)
Which technique is introduced to solve the problem of the penalty term penalizing small features heavily in ridge regression?

**Options:**
1. Standardization
2. Data augmentation
3. Feature selection
4. Normalization

**Answer:** Option 1: Standardization

*Explanation:* Standardization is the key technique used to address the issue of penalty term disproportionately affecting features with smaller scales in ridge regression. By scaling all features to have zero mean and unit variance, standardization ensures that the penalty term affects all features equally, regardless of their original scale.

## Question 2 (1 pt)
What is the formula for the z-score?

**Options:**
1. z = x – mean / standard deviation
2. z = x / standard deviation
3. z = x − mean
4. z = (x − mean) / standard deviation

**Answer:** Option 4: z = (x − mean) / standard deviation

*Explanation:* The z-score formula standardizes a value by subtracting the mean and dividing by the standard deviation. This transforms the data to have a mean of 0 and a standard deviation of 1, making different features comparable.

## Question 3 (1 pt)
Why is the StandardScaler used in ridge regression?

**Options:**
1. To remove irrelevant features from the dataset
2. To ensure that all features contribute equally to the penalty term by scaling features to have zero mean and unit variance
3. To convert categorical variables into numerical variables
4. To increase the size of the dataset by generating new data points

**Answer:** Option 2: To ensure that all features contribute equally to the penalty term by scaling features to have zero mean and unit variance

*Explanation:* StandardScaler is used in ridge regression to standardize features, ensuring that the L2 penalty term affects all features equally regardless of their original scale. This is crucial because ridge regression's penalty term is scale-dependent.

---

## Answer Key
1. Option 1: Standardization (Addresses penalty term scale sensitivity in ridge regression)
2. Option 4: z = (x − mean) / standard deviation (Standard formula for z-score normalization)
3. Option 2: Features scaled to zero mean and unit variance (Ensures equal penalty contribution in ridge regression)