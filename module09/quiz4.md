# Ridge Regression Quiz

## Question 1 (1 point)
Which of the following statements about ridge regression is correct?

**Options:**
1. Ridge regression does not use the alpha term for regularization.
2. Ridge regression results in sparse models by eliminating some predictors.
3. Ridge regression is used to prevent overfitting by adding a penalty to the regression coefficients.
4. In ridge regression, the penalty term does not depend on the size of alpha.

**Answer:** Option 3: Ridge regression is used to prevent overfitting by adding a penalty to the regression coefficients.

*Explanation:* Ridge regression fundamentally adds an L2 regularization term (penalty) to the cost function to prevent overfitting. This penalty term shrinks the coefficients toward zero but does not eliminate them completely, unlike Lasso regression.

## Question 2 (1 point)
In ridge regression, what is the alpha multiplied by the sum of θ₁² + θ₂² + ... + θᵢ² often called?

**Options:**
1. Residual sum of squares term
2. Error term
3. Bias term
4. Regularization term

**Answer:** Option 4: Regularization term

*Explanation:* In ridge regression, the term α(θ₁² + θ₂² + ... + θᵢ²) is the regularization term, also known as the L2 penalty term. This term controls the model's complexity by penalizing large coefficient values.

## Question 3 (1 point)
In ridge regression, how does the size of the alpha term affect the model's behavior?

**Options:**
1. A larger alpha increases the model's flexibility, allowing it to fit the training data more closely.
2. A larger alpha has no effect on the model's behavior.
3. A larger alpha reduces the complexity of the model by shrinking the coefficients toward zero.
4. A larger alpha decreases the penalty on the coefficients, leading to more overfitting.

**Answer:** Option 3: A larger alpha reduces the complexity of the model by shrinking the coefficients toward zero.

*Explanation:* The alpha parameter in ridge regression is the regularization strength. As alpha increases, the penalty on large coefficients becomes stronger, forcing them closer to zero and resulting in a simpler, more regularized model.

---

## Answer Key
1. Option 3 - Ridge regression uses penalty for overfitting prevention (Adds L2 regularization to cost function)
2. Option 4 - Regularization term (α(θ₁² + θ₂² + ... + θᵢ²) controls model complexity)
3. Option 3 - Larger alpha reduces model complexity (Stronger regularization shrinks coefficients)