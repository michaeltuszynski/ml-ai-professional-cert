# Quiz 3: Probability and Prediction in Scikit-learn

## Question 1 (1 point)
What does the predict_proba function in scikit-learn provide?

**Options:**
1. It returns the probability estimates for each class, indicating the confidence of the model.
2. It calculates the feature importance scores.
3. It returns the predicted class label for a given sample.
4. It computes the MSE for regression tasks.

**Answer:** Option 1: It returns the probability estimates for each class, indicating the confidence of the model.

*Explanation:* The `predict_proba()` function in scikit-learn returns probability estimates for each class in a classification task. These probabilities represent the model's confidence in its predictions for each possible class outcome.

---

## Question 2 (1 point)
What multiple of probabilities will the predict_proba() function return for a nearest neighbor model with k = 10?

**Options:**
1. 1
2. 0.01
3. 0.2
4. 0.1

**Answer:** Option 4: 0.1

*Explanation:* For a k-nearest neighbors model with k=10, the probabilities returned by `predict_proba()` will be multiples of 1/k = 1/10 = 0.1, as each neighbor contributes equally to the probability estimate.

---

## Question 3 (1 point)
How does scikit-learn classify binary predictions based on probability 𝑝?

**Options:**
1. Always predicts class 1
2. Class 0 if 𝑝 ≤ 0.5, class 1 if 𝑝 > 0.5
3. Class 1 if 𝑝 ≤ 0.5, class 0 if 𝑝 > 0.5
4. Always predicts class 0

**Answer:** Option 2: Class 0 if 𝑝 ≤ 0.5, class 1 if 𝑝 > 0.5

*Explanation:* In scikit-learn's binary classification, the default decision boundary is 0.5. Probabilities less than or equal to 0.5 are classified as class 0, while probabilities greater than 0.5 are classified as class 1.

---

## Answer Key
1. Option 1 - Probability estimates for each class (Returns model's confidence in predictions)
2. Option 4 - 0.1 (Based on 1/k where k=10 for k-nearest neighbors)
3. Option 2 - Class 0 if 𝑝 ≤ 0.5, class 1 if 𝑝 > 0.5 (Standard binary classification threshold)