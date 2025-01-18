# Model Complexity and Error Quiz

## Question 1 (1 point)
Which statement accurately describes the relationship between model complexity and error?

**Options:**
1. Model complexity and error are unrelated
2. Increasing model complexity typically increases error
3. Decreasing model complexity decreases error
4. Increasing model complexity generally decreases error

**Answer:** Option 2: Increasing model complexity typically increases error
*Explanation:* While increasing model complexity decreases training error, it typically increases error on unseen data (test/validation error) due to overfitting. This is a fundamental concept in machine learning known as the bias-variance tradeoff - as model complexity increases beyond an optimal point, the model becomes too specialized to the training data and performs poorly on new data.

---

## Question 2 (1 point)
Which of the following best describes overfitting in a general context?

**Options:**
1. Overfitting happens when a model learns the noise and details of the data too well, making it less effective at predicting new, unseen data
2. Overfitting is when a model's complexity is perfectly balanced to capture both the details and the general patterns in the data
3. Overfitting occurs when a model is too simple and fails to capture the underlying patterns in the data
4. Overfitting is when a model ignores the details of the data and only captures the general trends

**Answer:** Option 1: Overfitting happens when a model learns the noise and details of the data too well, making it less effective at predicting new, unseen data
*Explanation:* This is the fundamental definition of overfitting - when a model becomes too specialized to the training data, capturing noise rather than true patterns, which reduces its generalization ability.

---

## Question 3 (1 point)
Which of the following statements accurately describes the relationship between model complexity and variance?

**Options:**
1. Model complexity and variance are unrelated
2. Increasing model complexity generally decreases variance
3. Increasing model complexity typically increases variance
4. Decreasing model complexity increases variance

**Answer:** Option 3: Increasing model complexity typically increases variance
*Explanation:* As model complexity increases, the model becomes more flexible and can fit the training data more closely, leading to higher variance in predictions across different datasets.

---

## Answer Key
1. Option 2 - Increasing model complexity typically increases error (Fundamental relationship in ML, though beware of overfitting)
2. Option 1 - Overfitting occurs when model learns noise in training data (Core definition of overfitting)
3. Option 3 - Increasing complexity increases variance (Key concept in bias-variance tradeoff)