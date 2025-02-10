# Quiz 3: Ensemble Learning and Bootstrap Sampling

## Question 1 (1 point)
If the base model has high variance, what is a common solution in ensemble learning?

**Options:**
1. Use a single model with more features
2. Increase the complexity of the base model
3. Use bagging to combine multiple base models
4. Decrease the amount of training data

**Answer:** Option 3: Use bagging to combine multiple base models

*Explanation:* Bagging (Bootstrap Aggregating) is specifically designed to reduce variance in high-variance models. By training multiple models on different bootstrap samples and averaging their predictions, bagging effectively reduces overfitting while maintaining the model's ability to capture complex patterns.

## Question 2 (1 point)
What method is used for sampling in bootstrap sampling?

**Options:**
1. Without replacement
2. With replacement
3. Simple sampling
4. Cluster sampling

**Answer:** Option 2: With replacement

*Explanation:* Bootstrap sampling is fundamentally defined as sampling with replacement. This means that after an observation is selected and added to the sample, it is returned to the original dataset and can be selected again. This is essential for creating multiple different training sets from the same original data.

## Question 3 (1 point)
What is the chance of an item being included at least once in the bootstrap sample in N trials?

**Options:**
1. 1 − (1 – 1 / N)N
2. 1 − (1 / N)N
3. (1 –  1 / N)N
4. 1 / N

**Answer:** Option 1: 1 − (1 – 1 / N)N

*Explanation:* This probability is calculated by:
1. Finding the probability of NOT selecting an item in one trial: (1 - 1/N)
2. For N trials, probability of never selecting: (1 - 1/N)N
3. Therefore, probability of selecting at least once: 1 - (1 - 1/N)N

---

## Answer Key
1. Option 3 - Use bagging to combine multiple base models (Reduces variance through ensemble averaging)
2. Option 2 - With replacement (Fundamental definition of bootstrap sampling)
3. Option 1 - 1 − (1 – 1 / N)N (Probability calculation for bootstrap sample inclusion)
