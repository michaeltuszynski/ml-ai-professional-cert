# Quiz 3: Logistic Regression

## Question 1
You are given a model with two features, x₁ and x₂, as well as a categorical class, y. In the logistic function for this model, what would Z be equal to?

1. Z = β₁ + β₂x₁ + β₃x₂
2. Z = β₀ + β₁x₁
3. Z = β₀ + β₁x₁ + β₂x₂
4. Z = β₁x₁ + β₂x₂

**Correct Answer:** 3

**Explanation:** In logistic regression, Z represents the linear combination of features. For a model with two features, it must include:
- A bias term (β₀) which allows the model to fit data that doesn't pass through the origin
- One coefficient for each feature (β₁x₁ and β₂x₂)
Therefore, Z = β₀ + β₁x₁ + β₂x₂ is the correct form.

## Question 2
Is regularization strictly needed for logistic regression, or is it beneficial for better model performance?

1. Regularization is detrimental to model accuracy.
2. Regularization is not needed, as it has no impact on model performance.
3. Regularization is beneficial for better model performance.
4. Regularization is strictly needed for logistic regression.

**Correct Answer:** 3

**Explanation:** Regularization is beneficial but not mandatory for logistic regression because:
- It helps prevent overfitting by penalizing large coefficients
- It improves model generalization, especially with high-dimensional data
- It can handle multicollinearity better
However, it's not strictly required for the model to function, making option 3 the correct choice.

## Question 3
When initializing a LogisticRegression() object, which constructor parameter should be set to achieve LASSO (L1) regularization?

1. penalty='elasticnet'
2. penalty='l2'
3. penalty='none'
4. penalty='l1'

**Correct Answer:** 4

**Explanation:** LASSO (Least Absolute Shrinkage and Selection Operator) regularization:
- Uses the L1 norm penalty
- Is implemented in scikit-learn using penalty='l1'
- Can perform feature selection by potentially setting some coefficients to exactly zero
- Differs from L2 (Ridge) regularization which uses the squared magnitude of coefficients
