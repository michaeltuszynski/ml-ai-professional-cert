# Quiz 2: Logistic Regression Concepts

## Question 1 (1 point)
Assume that you have a single feature and two classes. What do you call the ratio of the area of class?

1. Class ratio
2. Odds ratio
3. Even ratio
4. Div ratio

**Correct Answer: 2**

*Explanation: The odds ratio is the correct term because it represents the relative likelihood of an outcome between two classes. In logistic regression, it measures the association between a feature and the outcome by comparing the odds of the outcome in different groups.*

## Question 2 (1 point)
In logistic regression, how is the odds ratio related to the linear expression?

1. The odds ratio is equal to the linear expression
2. The odds ratio is the square root of the linear expression
3. The odds ratio is the logarithm of the linear expression
4. The odds ratio is the exponential of the linear expression

**Correct Answer: 4**

*Explanation: The odds ratio is the exponential of the linear expression (eβ) because logistic regression uses the logit link function. When we take the exponential of the coefficient (β), we get the odds ratio, which tells us how much the odds change for a one-unit increase in the predictor variable.*

## Question 3 (1 point)
What is the formula used for sigmoidal function in logistic regression?

1. 1 / (1 + x)
2. eZ / (1 + eZ)
3. 1 / (1 + e-Z)
4. x² + 2x + 1

**Correct Answer: 3**

*Explanation: The sigmoid function 1/(1 + e^-Z) is used in logistic regression because it maps any real-valued input to a value between 0 and 1, making it perfect for binary classification. This S-shaped curve approaches 0 for very negative values and 1 for very positive values, naturally representing probabilities.*
