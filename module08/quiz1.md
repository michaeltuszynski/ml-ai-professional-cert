# Module 8 Quiz 1: Linear Regression and Feature Engineering

## Question 1 (1 point)
How does the linear regression model predict an output ŷ given three features, x₁, x₂, and x₃, along with their corresponding coefficients, β₁, β₂, and β₃?

**Options:**
1. ŷ = β₀ + β₁x₁ + β₂x₂ + β₃x₃
2. ŷ = β₁x₁ + β₂x₂ + β₃x₃
3. ŷ = β₀ + β₁x₁
4. ŷ = β₀

**Answer:** Option 1: ŷ = β₀ + β₁x₁ + β₂x₂ + β₃x₃

*Explanation:* The linear regression model predicts output as a linear combination of all input features plus an intercept term (β₀). Each feature xᵢ is multiplied by its corresponding coefficient βᵢ, and these terms are summed together with the intercept. This is the fundamental definition of multiple linear regression.

## Question 2 (1 point)
What is the use of including a squared regression term in the linear regression model while fitting?

**Options:**
1. To ensure the model remains simple and interpretable
2. To increase the number of features without any specific reason
3. To capture nonlinear relationships between variables
4. To eliminate the need for an intercept term

**Answer:** Option 3: To capture nonlinear relationships between variables

*Explanation:* Squared terms are added to linear regression models to capture nonlinear (specifically, quadratic) relationships in the data. When the relationship between variables follows a curved pattern rather than a straight line, adding squared terms allows the linear regression framework to model these parabolic relationships effectively. Option 4 is incorrect because the intercept term (β₀) remains essential for capturing the baseline level of the dependent variable - squared terms help model curvature but do not replace the need for an intercept. Option 1 is incorrect as adding squared terms actually makes the model more complex. Option 2 is incorrect as squared terms are added with a specific purpose, not arbitrarily.

## Question 3 (1 point)
How do you include squared terms in a linear regression model?

**Options:**
1. Taking the square of the feature in the linear regression model equation
2. Using the SquaredRegression library from scikit-learn
3. Adding a new column with squared values of the feature
4. Adding a new row with squared values of the feature

**Answer:** Option 3: Adding a new column with squared values of the feature

*Explanation:* To include squared terms in a linear regression model, you create a new feature column containing the squared values of the original feature. This is done through feature engineering - transforming the input data while still using the standard linear regression framework. Option 4 is incorrect because adding new rows would only increase the number of data points, not create squared features. Option 2 is incorrect as there is no special "SquaredRegression" library needed - standard linear regression is used with transformed features. Option 1 is incorrect because merely writing the square in the equation isn't sufficient - the actual data transformation is needed.

---

## Answer Key
1. Option 1 - ŷ = β₀ + β₁x₁ + β₂x₂ + β₃x₃
   (Correct: Includes all features and intercept term; other options miss essential components)

2. Option 3 - To capture nonlinear relationships between variables
   (Correct: Squared terms model curved relationships; other options either misstate the purpose or suggest incorrect effects like eliminating intercept terms)

3. Option 3 - Adding a new column with squared values of the feature
   (Correct: Proper implementation through feature engineering; other options either suggest incorrect data manipulation or non-existent libraries)