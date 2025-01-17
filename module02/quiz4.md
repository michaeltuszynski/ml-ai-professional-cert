# Data Analysis Tools Quiz

## Question 1 (1 point)
In Python, what would you use to generate a covariance matrix on a DataFrame?

**Options:**
1. df.head()
2. df.cov()
3. df.describe()
4. df.corr()

**Answer:** Option 2: df.cov()

*Explanation:* The `df.cov()` method in pandas computes the pairwise covariance matrix of the DataFrame's columns. The covariance matrix shows how each variable varies with respect to every other variable, with diagonal elements representing variances of individual variables.

---

## Question 2 (1 point)
In Python, what is the output of the given statement df.corr()?

**Options:**
1. Diagonal matrix
2. Correlation plot
3. Correlation matrix
4. Covariance matrix

**Answer:** Option 3: Correlation matrix

*Explanation:* The `df.corr()` method returns a correlation matrix, which contains correlation coefficients between -1 and 1 for all pairs of columns in the DataFrame. The diagonal elements are always 1 (perfect self-correlation), and the matrix is symmetric.

---

## Question 3 (1 point)
In a correlation matrix, the correlation coefficient value close to 1 (e.g., 0.95) is indicative of which type of correlation?

**Options:**
1. No correlation between the variables
2. A strong positive correlation between the variables
3. No correlation between the variables
4. A strong negative correlation between the variables

**Answer:** Option 2: A strong positive correlation between the variables

*Explanation:* A correlation coefficient close to 1 (like 0.95) indicates a strong positive correlation, meaning the two variables tend to increase or decrease together. The closer to 1, the stronger the positive linear relationship between the variables.

---

## Question 4 (1 point)
Given two random variables, X and Y, what does the conditional probability P(X|Y) represent?

**Options:**
1. The probability of Y occurring given that X has occurred
2. The joint probability of both X and Y occurring
3. The probability of X occurring given that Y has occurred
4. The marginal probability of X occurring

**Answer:** Option 3: The probability of X occurring given that Y has occurred

*Explanation:* The conditional probability P(X|Y) represents the probability of X occurring, given that we know Y has occurred. This is a fundamental concept in probability theory that helps us understand how the probability of one event is affected by the knowledge of another event's occurrence.

---

# Answer Key
1. Option 2 - df.cov() (Generates covariance matrix showing pairwise relationships)
2. Option 3 - Correlation matrix (Shows standardized relationships between variables)
3. Option 2 - Strong positive correlation (Variables move together in same direction)
4. Option 3 - P(X|Y) (Probability of X given Y has occurred)