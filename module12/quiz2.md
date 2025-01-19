# K-Nearest Neighbors Quiz

## Question 1 (1 point)
What is the misclassification error in k-nearest neighbors?

**Options:**
1. The error resulting from using a non-Euclidean distance metric
2. The error caused by choosing an inappropriate value of k
3. The error introduced due to noisy data points
4. The proportion of misclassified instances in the test set

**Answer:** Option 4: The proportion of misclassified instances in the test set

**Explanation:** The misclassification error is fundamentally the percentage of incorrect predictions in the test set. While other factors like distance metrics (1), k-value choice (2), and noisy data (3) can contribute to misclassification, the term specifically refers to the proportion of wrong predictions.

---

## Question 2 (1 point)
For a small dataset, suppose four out of five predictions are correct. What would the misclassification rate be?

**Options:**
1. 5%
2. 10%
3. 30%
4. 20%

**Answer:** Option 4: 20%

**Explanation:** If 4 out of 5 predictions are correct, then 1 out of 5 is incorrect. To calculate the misclassification rate: (1/5) × 100 = 20%.

---

## Question 3 (1 point)
A nearest neighbors model is built with different values of k, and the misclassification error is computed on each value of k. On what basis is the best possible k selected?

**Options:**
1. Zero error
2. Least MSE
3. Least misclassification error
4. Highest misclassification error

**Answer:** Option 3: Least misclassification error

**Explanation:** When selecting the optimal k value in KNN, we choose the k that produces the lowest misclassification error on the validation set. This indicates the model's best performance in correctly classifying instances.

---

## Answer Key
1. Option 4 - The proportion of misclassified instances in the test set (Core definition of misclassification error)
2. Option 4 - 20% (Simple calculation: 1 wrong out of 5 = 20% error rate)
3. Option 3 - Least misclassification error (Standard method for optimizing k in KNN)