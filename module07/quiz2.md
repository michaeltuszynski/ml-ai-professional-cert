# Module 7 Quiz 2: Linear Regression Implementation

## Question 1 (1 point)
Which library(s) can be used to build a linear regression model in Python?

**Options:**
1. NumPy and pandas
2. Matplotlib and seaborn
3. TensorFlow and Keras
4. Scikit-learn

**Answer:** Option 4: Scikit-learn

*Explanation:* While other libraries can be used for data manipulation and visualization, scikit-learn is the primary library for implementing linear regression models in Python. It provides the `LinearRegression` class specifically designed for this purpose, with simple methods for model creation, training, and prediction.

---

## Question 2 (1 point)
Which of the following represents the correct sequence of steps for creating a linear regression model?

**Options:**
1. Fit the model, instantiate a linear model object, and make predictions
2. Fit the model, make predictions, and instantiate a linear model object
3. Instantiate a linear model object, fit the model, and make predictions
4. Instantiate a linear model object, make predictions, and fit the model

**Answer:** Option 3: Instantiate a linear model object, fit the model, and make predictions

*Explanation:* The correct sequence in scikit-learn is to first create the model object using `LinearRegression()`, then train it using `fit(features, target)`, and finally use it to make predictions with `predict(features)`. This sequence is essential as the model needs to be created before it can be trained, and it needs to be trained before it can make predictions.

---

## Question 3 (1 point)
Given a dataset with the outcome variable 'tip,' what is the command in Python library 'scikit-learn' to fit the model for the linear regression model?

**Options:**
1. f.fit(features)
2. f.fit(tip,features)
3. f(features,tip)
4. f.fit(features,tip)

**Answer:** Option 4: f.fit(features,tip)

*Explanation:* In scikit-learn, the `fit()` method takes two arguments: X (features) and y (target variable). The correct syntax is `model.fit(features, target)` where features come first, followed by the target variable (tip in this case). This follows scikit-learn's consistent API design where X (features) always comes before y (target).

---

# Answer Key
1. Option 4 - Scikit-learn (Primary library for implementing linear regression in Python)
2. Option 3 - Instantiate a linear model object, fit the model, and make predictions (Correct sequence for model creation and training)
3. Option 4 - f.fit(features,tip) (Proper syntax for fitting a scikit-learn model)