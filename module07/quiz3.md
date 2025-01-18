# Module 7 Quiz: Regression and Loss Functions

## Question 1 (1 point)
In regression, which of the following functions is specifically used to generate predictions for the outcome variable based on the input features of a trained model?

**Options:**
1. f.transform()
2. f.fit()
3. f.predict()
4. f.score()

**Answer:** Option 3: f.predict()

*Explanation:* The `predict()` method is specifically used to generate predictions from a trained model. After training a model with `fit()`, we use `predict()` to generate predictions for new input data. This is a core definition in scikit-learn's API, distinct from `transform()` (for feature transformation), `fit()` (for training), or `score()` (for model evaluation).

## Question 2 (1 point)
What is the L2 loss function for a linear regression?

**Options:**
1. (data["feature"]-data["prediction"])*2
2. (data["feature"]-data["prediction"])**2
3. (data["feature"]+data["prediction"])**2
4. (data["feature"]-data["prediction"])

**Answer:** Option 2: (data["feature"]-data["prediction"])**2

*Explanation:* The L2 (squared) loss is defined as (y - ŷ)², where y is the actual value and ŷ is the prediction. This is the fundamental definition of L2 loss, which measures the squared difference between actual and predicted values.

## Question 3 (1 point)
What is the MSE of a linear regression model?

**Options:**
1. The maximum difference between actual and predicted values
2. The sum of the differences between actual and predicted values
3. The average of the absolute differences between actual and predicted values
4. The average of the squared differences between actual and predicted values

**Answer:** Option 4: The average of the squared differences between actual and predicted values

*Explanation:* The mean squared error (MSE) is the average of the square of the distance of each data point from our model's regression line. This is the core definition of MSE, which takes the average of all L2 losses across the dataset.

## Question 4 (1 point)
What would be the most optimal value of θ in a plot that shows the MSE plotted against different values of θ?

**Options:**
1. The value of θ where the MSE is the average
2. The value of θ where the MSE is constant
3. The value of θ where the MSE is maximum
4. The value of θ where the MSE is minimum

**Answer:** Option 4: The value of θ where the MSE is minimum

*Explanation:* The optimal θ is the one that minimizes the MSE, as this represents the best fit of the model to the data. When plotting MSE against θ values, we look for the minimum point which indicates the optimal parameter value.

---

# Answer Key
1. Option 3 - f.predict() (Used to generate predictions from trained model)
2. Option 2 - (data["feature"]-data["prediction"])**2 (Definition of L2 loss)
3. Option 4 - The average of the squared differences (Definition of MSE)
4. Option 4 - The value of θ where the MSE is minimum (Optimal parameter value)