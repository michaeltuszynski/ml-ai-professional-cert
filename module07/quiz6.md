# Multiple Linear Regression Quiz

## Question 1 (1 point)
What is the primary purpose of adding more than one predictor variable in multiple linear regression?

**Options:**
1. To simplify the model and improve interpretability
2. To increase the complexity of the model
3. To decrease computational resources required for model training
4. To reduce overfitting and improve model performance

**Answer:** Option 4: To reduce overfitting and improve model performance

*Explanation:* Multiple predictor variables in linear regression allow the model to capture more complex relationships in the data, potentially leading to better predictions and reduced overfitting by accounting for multiple relevant factors that influence the outcome variable.

---

## Question 2 (1 point)
What is the command in Python that retrieves the coefficients of a regression model?

**Options:**
1. model.coefficients
2. model.params
3. model.coef_
4. model.intercept_

**Answer:** Option 3: model.coef_

*Explanation:* In scikit-learn's implementation of regression models, `model.coef_` is the standard attribute that returns the coefficients of the features in the model. This is distinct from `model.intercept_` which returns the bias term.

---

## Question 3 (1 point)
Suppose that the outcome variable is 'tip,' the features are "Features = data[["bill","size"]]", and the coefficients for the features are [0.1, 0.3]. What will the linear equation for the outcome variable be?

**Options:**
1. tip = 0.1*bill + 0.3*size
2. tip = 0.3*size
3. tip = 0.1*bill
4. tip = 0.3*bill + 0.1*size

**Answer:** Option 1: tip = 0.1*bill + 0.3*size

*Explanation:* In multiple linear regression, the coefficients are applied in the order of the features array. Since the features are ["bill", "size"] and coefficients are [0.1, 0.3], the first coefficient (0.1) corresponds to 'bill' and the second coefficient (0.3) corresponds to 'size'.

---

## Answer Key
1. Option 4 - To reduce overfitting and improve model performance (Captures complex relationships while maintaining model performance)
2. Option 3 - model.coef_ (Standard scikit-learn attribute for accessing model coefficients)
3. Option 1 - tip = 0.1*bill + 0.3*size (Coefficients match feature order in the input array)