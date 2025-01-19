# Kernel Functions in Machine Learning Quiz

## Question 1 (1 point)
What is a kernel in the context of ML?

**Options:**
1. It is a function that transforms data vectors into a higher-dimensional space
2. It is a function that calculates the distance between two data vectors
3. It is a function that performs data normalization before training a model
4. It is a function that takes two data vectors as input and returns a scalar value

**Answer:** Option 4 - A kernel is a function that takes two data vectors as input and returns a scalar value. The key insight of the kernel trick is that it computes the similarity (inner product) between two points in a higher-dimensional space without explicitly transforming the data into that space. This makes kernel methods computationally efficient while still capturing non-linear relationships in the data.

---

## Question 2 (1 point)
What is the equation given below called?

```
k(x,z) = (xᵀz + 1)²
```

**Options:**
1. Gaussian kernel function
2. Linear kernel function
3. Quadratic kernel function
4. Polynomial kernel function

**Answer:** Option 3 - This is a quadratic kernel function. The equation shows a specific case where the inner product of vectors x and z plus a constant (1) is squared. This is distinct from a general polynomial kernel as it specifically uses degree 2 (quadratic) and has a specific form optimized for quadratic relationships in the data.

---

## Question 3 (1 point)
What is the function in the Python library scikit-learn to build a Gaussian kernel?

**Options:**
1. rbf_kernel()
2. polynomial_kernel()
3. linear_kernel()
4. ridge_kernel()

**Answer:** Option 1 - The `rbf_kernel()` function in scikit-learn is used to compute the Gaussian (RBF) kernel between two matrices. RBF stands for Radial Basis Function, which is another name for the Gaussian kernel.

---

# Answer Key
1. Option 4 - Function that takes two vectors as input and returns their similarity as a scalar
2. Option 3 - Quadratic kernel function
3. Option 1 - rbf_kernel()