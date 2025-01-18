# Quiz 5: Model Complexity and Parameters

## Question 1 (1 point)
What would the mean squared error (MSE) be for a model with N data points and a polynomial regression model with degree N − 1?

**Options:**
1. 1
2. It varies depending on the dataset
3. It cannot be determined
4. 0

**Answer:** Option 4: 0

*Explanation:* A polynomial of degree N-1 has N parameters, allowing it to perfectly fit N data points, resulting in zero error. This is a fundamental mathematical property, though such perfect fitting typically indicates overfitting.

## Question 2 (1 point)
How many coefficients are computed for an N-dimensional model using linear regression?

**Options:**
1. N
2. N − 1
3. N + 1
4. 2N

**Answer:** Option 3: N + 1

*Explanation:* In linear regression with N features, we have N coefficients (one for each feature) plus one intercept term, totaling N + 1 coefficients.

## Question 3 (1 point)
How is overfitting affected by the number of parameters in a machine learning model?

**Options:**
1. Overfitting decreases as the number of parameters in the model increases
2. Overfitting tends to decrease initially as the number of parameters increases, but then it increases after a certain point
3. Overfitting remains constant regardless of the number of parameters in the model
4. Overfitting increases as the number of parameters in the model decreases

**Answer:** Option 2: Overfitting tends to decrease initially as the number of parameters increases, but then it increases after a certain point

*Explanation:* This represents the bias-variance tradeoff. Initially, more parameters help the model better fit the true underlying pattern (reducing underfitting). However, beyond a certain point, too many parameters cause the model to fit noise in the training data, leading to overfitting.

---

## Answer Key
1. Option 4 - 0 (Perfect fit with N parameters for N points)
2. Option 3 - N + 1 (N feature coefficients plus intercept)
3. Option 2 - Overfitting follows a U-shaped curve with model complexity (bias-variance tradeoff)