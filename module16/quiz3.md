# Support Vector Machines Quiz

## Question 1 (1 point)
What does the "margin" refer to in the context of a maximum margin classifier?

**Options:**
1. The number of support vectors identified during training
2. The distance between the decision boundary (hyperplane) and the nearest data points (support vectors) from each class
3. The number of features used in the classification model
4. The distance between any two randomly selected data points in the dataset

**Answer:** Option 2 - The distance between the decision boundary (hyperplane) and the nearest data points (support vectors) from each class

*Core Definition:* The margin is the perpendicular distance from the decision boundary to the nearest training data points on either side.

*Additional Context:* In SVMs, we aim to maximize this margin to create the most robust possible classifier, as a larger margin generally leads to better generalization.

---

## Question 2 (1 point)
What does the "margin" of a decision boundary represent in a classification context?

**Options:**
1. The average distance from the decision boundary to all data points in the training set
2. The total number of data points correctly classified by the decision boundary
3. The number of dimensions in the feature space used to define the decision boundary
4. The perpendicular distance from the decision boundary to the nearest data point in the training set

**Answer:** Option 4 - The perpendicular distance from the decision boundary to the nearest data point in the training set

*Core Definition:* The margin represents the smallest perpendicular distance between the decision boundary and any training point.

*Additional Context:* This definition ensures the classifier maintains maximum separation between classes while being determined by the most critical points (support vectors).

---

## Question 3 (1 point)
In a maximum margin classifier, what is the relationship between the support vectors and the optimization problem?

**Options:**
1. Support vectors are outliers minimized by the optimization process
2. Support vectors are randomly selected for optimization adjustments
3. Support vectors highlight features optimized in the classifier
4. Support vectors define the boundary, and the optimization maximizes their separation

**Answer:** Option 4 - Support vectors define the boundary, and the optimization maximizes their separation

*Core Definition:* Support vectors are the critical points that lie exactly on the margin and directly influence the position of the decision boundary.

*Additional Context:* The optimization problem in SVMs specifically works to maximize the margin while ensuring these support vectors are correctly classified, as they are the only points that matter for defining the optimal hyperplane.

---

## Question 4 (1 point)
What do you call the data points that are used to determine the margin in a maximum margin classifier?

**Options:**
1. Support vectors
2. Pivots
3. Anchors
4. Focal points

**Answer:** Option 1 - Support vectors

*Core Definition:* Support vectors are the data points that lie exactly on the margin boundaries and are used to determine the optimal hyperplane.

*Additional Context:* These points are called "support" vectors because they literally support the margin boundaries and are the only points needed to fully define the classifier.

---

# Answer Key
1. Option 2 - Distance between decision boundary and nearest points
2. Option 4 - Perpendicular distance to nearest data point
3. Option 4 - Support vectors define boundary and optimization maximizes separation
4. Option 1 - Support vectors