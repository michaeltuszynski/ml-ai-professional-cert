# Decision Tree Classifier Quiz

## Question 1 (1 point)
### What happens to the training accuracy of a decision tree classifier when the data points overlap exactly?

1. The training accuracy cannot be determined.
2. The training accuracy is less than 100%.
3. The training accuracy is greater than 100%.
4. The training accuracy is 100%.

**Correct Answer: 2**

*Explanation: When data points overlap exactly but belong to different classes, the decision tree cannot achieve 100% training accuracy because it cannot perfectly separate overlapping points with different labels. This results in a training accuracy less than 100%.*

---

## Question 2 (1 point)
### From the plot of the decision tree, how do you infer whether the model is overfitted?

1. Overfitting cannot be determined from the tree plot.
2. If the tree has few levels (shallow), it is likely to be overfitted.
3. The number of nodes in the tree does not affect overfitting.
4. If the tree has many levels (deep), it is likely to be overfitted.

**Correct Answer: 4**

*Explanation: A deep decision tree with many levels typically indicates overfitting, as it suggests the model has learned very specific patterns in the training data, potentially including noise.*

---

## Question 3 (1 point)
### Which statement about decision tree classifiers and feature count is correct?

1. Decision tree classifiers are not affected by the number of features used for training.
2. Increasing the number of features never affects the performance of decision tree classifiers.
3. Adding more features always leads to overfitting because decision trees can easily capture noise in the data.
4. More features tend to lead to overfitting in decision tree classifiers due to increased model complexity.

**Correct Answer: 4**

*Explanation: More features increase the model's complexity and provide more opportunities for the tree to find patterns in noise, making it more susceptible to overfitting. However, this is a tendency rather than an absolute rule.*