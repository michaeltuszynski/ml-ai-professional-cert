# Quiz 6: Model Evaluation and Cross-Validation

## Question 1 (1 point)
Why is the function `get_MSE_for_degree_k_model` used?

**Options:**
1. To calculate the mean squared error (MSE) for a polynomial regression model of degree k.
2. To evaluate the goodness of fit of a linear regression model
3. To generate random samples from a Gaussian distribution.
4. To assess the performance of a model using the accuracy metric

**Answer:** Option 1: To calculate the mean squared error (MSE) for a polynomial regression model of degree k.

*Explanation:* The function specifically calculates MSE for polynomial regression models of varying degrees (k), which is essential for comparing model performance and complexity.

---

## Question 2 (1 point)
Considering the mean squared error (MSE) for both training and test datasets, what is the guiding principle in choosing the most appropriate model?

**Options:**
1. The model with an MSE closest to 0 on the test dataset and slightly higher on the training dataset is usually the most suitable.
2. The model with an MSE closest to 1 on the test dataset and slightly lower on the training dataset is usually the most suitable.
3. The model with the highest MSE on the test dataset and slightly lower on the training dataset is generally the most suitable
4. The model with the lowest MSE on the test dataset and slightly higher on the training dataset is typically the most suitable.

**Answer:** Option 4: The model with the lowest MSE on the test dataset and slightly higher on the training dataset is typically the most suitable.

*Explanation:* This indicates good generalization without overfitting, as the model performs well on unseen data while maintaining a reasonable training error.

---

## Question 3 (1 point)
What is cross-validation in the context of machine learning?

**Options:**
1. A method to reduce overfitting by training the model on the entire dataset and testing it on the same dataset
2. A process to increase training data by generating new samples from the existing dataset
3. A technique to improve model accuracy by using an additional dataset not seen during training
4. A method to evaluate model performance by splitting the training data into multiple subsets and using them for training and validation iteratively

**Answer:** Option 4: A method to evaluate model performance by splitting the training data into multiple subsets and using them for training and validation iteratively.

*Explanation:* Cross-validation is fundamentally a model validation technique that assesses how well a model will generalize to independent data by using different portions of the training data for training and validation.

---

## Question 4 (1 point)
What is the common shape of the validation error curve?

**Options:**
1. L-shaped
2. Straight-lined
3. Bowl-shaped
4. T-shaped

**Answer:** Option 3: Bowl-shaped

*Explanation:* The validation error curve typically follows a U-shaped or bowl-shaped pattern, where error initially decreases with model complexity but then increases due to overfitting.

---

# Answer Key
1. Option 1 - MSE calculation for polynomial models (Core function purpose for model evaluation)
2. Option 4 - Lowest test MSE with slightly higher training MSE (Indicates optimal model generalization)
3. Option 4 - Iterative training/validation splitting (Fundamental cross-validation definition)
4. Option 3 - Bowl-shaped (Characteristic validation error curve pattern)