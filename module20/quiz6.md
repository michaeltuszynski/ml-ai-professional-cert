# Module 20 Quiz 6: Boosting Algorithms

## Question 1 (1 point)
What is the correct Python statement to create an AdaBoost model with a decision tree as the base model?

**Options:**
1. `from sklearn.ensemble import AdaBoostClassifier(base_estimator=DecisionTreeClassifier())`
2. `from sklearn.ensemble import AdaBoostClassifier(base_model=DecisionTreeClassifier())`
3. `from sklearn.ensemble import AdaBoostClassifier(model=DecisionTreeClassifier())`
4. `from sklearn.ensemble import AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1))`

**Answer:** Option 4: `from sklearn.ensemble import AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=1))`

Explanation: In scikit-learn's AdaBoostClassifier, the parameter `base_estimator` is used to specify the base model. A decision tree with `max_depth=1` (also known as a decision stump) is commonly used as the base estimator for AdaBoost as it makes an effective weak learner.

---

## Question 2 (1 point)
What does gradient boosting refer to in the context of ML?

**Options:**
1. Applying gradient descent to the problem of boosting by combining multiple weak learners into a strong learner
2. Combining several boosting algorithms to create an ensemble model with gradient descent
3. Using a single strong model to perform boosting with a predefined learning rate
4. Applying gradient descent to the problem of boosting by using a single model to correct errors

**Answer:** Option 1: Applying gradient descent to the problem of boosting by combining multiple weak learners into a strong learner

Explanation: Gradient boosting is fundamentally an optimization technique that uses gradient descent to minimize a loss function by iteratively adding weak learners to create a strong ensemble model. Each new weak learner is trained to correct the errors of the previous ensemble.

---

## Question 3 (1 point)
What is the cost function for gradient boosting trees?

**Options:**
1. Cubic loss
2. Loss
3. Squared loss
4. Dividend loss

**Answer:** Option 3: Squared loss

Explanation: Squared loss (L2 loss) is the default and most commonly used cost function for gradient boosting regression trees. It measures the mean squared error between predictions and actual values, though other loss functions can be used depending on the specific problem requirements.

---

## Question 4 (1 point)
Which of the following is a property of boosting algorithms?

**Options:**
1. Boosting algorithms combine weak learners to create a stronger model
2. Boosting reduces the complexity of the model by removing features
3. Boosting always leads to overfitting regardless of the dataset
4. Boosting algorithms only work with linear models

**Answer:** Option 1: Boosting algorithms combine weak learners to create a stronger model

Explanation: The fundamental principle of boosting is to iteratively combine multiple weak learners (models that perform slightly better than random chance) into a strong ensemble model. This is achieved by giving more weight to misclassified examples in subsequent iterations.

---

## Answer Key
1. Option 4 (Using correct base_estimator parameter with decision stump)
2. Option 1 (Gradient descent optimization with weak learners)
3. Option 3 (Squared loss as default cost function)
4. Option 1 (Fundamental principle of combining weak learners)
