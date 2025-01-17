# Module 6 Quiz

## Question 1 (1 point)
What does the curse of dimensionality indicate?

**Options:**
1. A method for efficiently handling high-dimensional datasets
2. A phenomenon where algorithms perform better with an increase in the number of dimensions
3. The superiority of higher-dimensional data for clustering tasks
4. The exponential increase in computational complexity with the rise in dimensionality

**Answer:** Option 4: The exponential increase in computational complexity with the rise in dimensionality

*Explanation:* The curse of dimensionality refers to the fundamental challenge that arises when working with high-dimensional data. As the number of dimensions increases, the amount of data needed to make statistically sound predictions grows exponentially, making analysis computationally intensive and potentially intractable.

## Question 2 (1 point)
What does PCA look for in terms of linear combinations of existing features that capture the bulk of the variance?

**Options:**
1. Columns
2. Sets
3. Rows
4. Tuples

**Answer:** Option 1: Columns

*Explanation:* PCA (Principal Component Analysis) looks for linear combinations of the original features (columns) that maximize variance in the data. These new features (principal components) are created by finding directions in the feature space where the data varies the most.

## Question 3 (1 point)
What does running SVD on X decompose X into?

**Options:**
1. U Σ V
2. U
3. U Σ
4. Σ V

**Answer:** Option 1: U Σ V

*Explanation:* Singular Value Decomposition (SVD) decomposes a matrix X into the product of three matrices: U (left singular vectors), Σ (diagonal matrix of singular values), and V (right singular vectors transposed).

## Question 4 (1 point)
What is the formula to normalize a dataset X?

**Options:**
1. Xnorm = (X+μ)/σ
2. Xnorm = (X−μ)
3. Xnorm = X/σ
4. Xnorm = (X−μ)/σ

**Answer:** Option 4: Xnorm = (X−μ)/σ

*Explanation:* This is the standard score (z-score) normalization formula. It subtracts the mean (μ) and divides by the standard deviation (σ) to transform the data to have zero mean and unit variance.

## Question 5 (1 point)
Which NumPy function is used to determine whether two arrays are element-wise equal within a specified tolerance?

**Options:**
1. numpy.allclose
2. Numpy.array_equal
3. numpy.equal
4. Numpy.isclose

**Answer:** Option 1: numpy.allclose

*Explanation:* `numpy.allclose()` is the correct function for checking if all array elements are equal within a specified tolerance. It's particularly useful for floating-point comparisons where exact equality might fail due to numerical precision issues.

---

# Answer Key
1. Option 4 - The exponential increase in computational complexity with the rise in dimensionality (Fundamental challenge in high-dimensional data analysis)
2. Option 1 - Columns (PCA finds linear combinations of original features/columns)
3. Option 1 - U Σ V (Complete matrix decomposition in SVD)
4. Option 4 - Xnorm = (X−μ)/σ (Standard score normalization formula)
5. Option 1 - numpy.allclose (Function for approximate array equality comparison)