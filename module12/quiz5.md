# K-Nearest Neighbors Quiz

## Question 1 (1 pt)
What is the function in scikit-learn used for solving regression problems with nearest neighbors?

**Options:**
1. KRegressor()
2. KNeighborsClassifier()
3. KNearestRegressor()
4. KNeighborsRegressor()

**Answer:** Option 4: KNeighborsRegressor()

*Explanation:* `KNeighborsRegressor()` is the official scikit-learn implementation for k-NN regression. This class is specifically designed for predicting continuous values using the k-nearest neighbors algorithm, unlike `KNeighborsClassifier()` which is for classification tasks.

---

## Question 2 (1 pt)
What is the output of the predict() function for KNeighborsRegressor()?

**Options:**
1. A binary decision
2. A class label
3. A probability score
4. A continuous numeric value

**Answer:** Option 4: A continuous numeric value

*Explanation:* The `predict()` method in `KNeighborsRegressor()` returns continuous numeric values since it's a regression model. It calculates this by averaging the target values of its k-nearest neighbors, unlike classification which returns discrete class labels.

---

## Question 3 (1 pt)
Which metric should be used as cross-validation for KNeighborsRegressor to find the optimal value of k?

**Options:**
1. ROC AUC
2. F1 score
3. MSE
4. Accuracy

**Answer:** Option 3: MSE

*Explanation:* Mean Squared Error (MSE) is the appropriate metric for evaluating regression models like KNeighborsRegressor. ROC AUC, F1 score, and accuracy are classification metrics and don't apply to regression problems where we're predicting continuous values.

---

## Answer Key
1. Option 4: KNeighborsRegressor() (The official scikit-learn class for k-NN regression)
2. Option 4: A continuous numeric value (Regression models predict continuous values)
3. Option 3: MSE (Standard metric for evaluating regression model performance)