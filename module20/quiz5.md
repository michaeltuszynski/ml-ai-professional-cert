# Quiz 5: Decision Trees and Weight Updates

## Question 1 (1 point)
What do you call a tree with only one node that slices the dataset in alignment with one of the features?

**Options:**
1. Decision algorithm
2. Decision stump
3. Decision node
4. Decision tree

**Answer:** Option 2: Decision stump

A decision stump is a one-level decision tree that makes a single split on one feature, serving as the simplest form of a decision tree classifier.

---

## Question 2 (1 point)
Which of the following correctly describes the misclassification score ϵs of a decision stump?

**Options:**
1. The sum of the weights of all misclassified samples
2. The sum of the weights of misclassified samples divided by the sum of all sample weights
3. The average weight of all samples
4. The sum of the weights of misclassified samples using an incorrect notation for weights

**Answer:** Option 1: The sum of the weights of all misclassified samples

The misclassification score ϵs is the absolute sum of weights for all misclassified samples, representing the total weighted error without normalization. This is distinct from normalized error rates which would divide by the total weight sum.

---

## Question 3 (1 point)
In the context of updating sample weights with the influence parameter αs​, what happens to the weight of a sample that was correctly classified?

**Options:**
1. The weight is decreased by αs
2. The weight is set to zero
3. The weight remains unchanged
4. The weight is increased by αs

**Answer:** Option 1: The weight is decreased by αs

In boosting algorithms like AdaBoost, the weights of correctly classified samples are decreased by the influence parameter αs to reduce their impact on subsequent classifiers, while misclassified samples' weights are increased.

---

## Answer Key
1. Option 2: Decision stump (A single-node decision tree that splits on one feature)
2. Option 1: The sum of the weights of all misclassified samples (Raw weighted error score without normalization)
3. Option 1: The weight is decreased by αs (Weight adjustment in boosting algorithms)
