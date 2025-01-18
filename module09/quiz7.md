# Quiz 7: LASSO Regression and Regularization

## Question 1 (1 pt)
What is LASSO regression also known as?

**Options:**
1. Elastic net regularization
2. L2 regularization
3. L1 regularization
4. Ridge regression

**Answer:** Option 3: L1 regularization

LASSO (Least Absolute Shrinkage and Selection Operator) regression is fundamentally defined as L1 regularization. This refers to the use of L1 norm for the penalty term in the regularization process.

---

## Question 2 (1 pt)
What is the penalty term in L1 regularization?

**Options:**
1. The sum of the parameters multiplied by alpha
2. The sum of the squares of the parameters multiplied by alpha
3. The product of the parameters and alpha
4. The sum of the absolute values of the parameters multiplied by alpha

**Answer:** Option 4: The sum of the absolute values of the parameters multiplied by alpha

L1 regularization's penalty term is mathematically defined as α∑|βᵢ|, where α is the regularization parameter and βᵢ are the model parameters.

---

## Question 3 (1 pt)
What is the regression that forces the parameters to be smaller and, in most circumstances, forces many of its parameters to zero?

**Options:**
1. Ridge regression
2. Linear regression
3. Logistic regression
4. LASSO regression

**Answer:** Option 4: LASSO regression

LASSO regression's key characteristic is its ability to perform both regularization and feature selection by shrinking coefficients to exactly zero, unlike Ridge regression which only shrinks coefficients close to zero.

---

# Answer Key
1. Option 3: L1 regularization (LASSO's fundamental mathematical framework)
2. Option 4: Sum of absolute values of parameters × alpha (Definition of L1 penalty term)
3. Option 4: LASSO regression (Unique property of coefficient shrinkage to zero)