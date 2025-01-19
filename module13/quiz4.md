# Quiz 4: Multiclass Classification Methods

## Question 1
**Which of the following is NOT a method for adapting binary classification models to multiclass problems?**

1. One-vs-zero
2. One-vs-one
3. Multinomial regression
4. One-vs-rest

**Correct Answer: 1**

**Explanation:** "One-vs-zero" is not a real multiclass classification method. The standard approaches are:
- One-vs-one (OvO): Creates binary classifiers for each pair of classes
- One-vs-rest (OvR)/One-vs-all (OvA): Creates binary classifiers comparing each class against all others
- Multinomial regression: Directly handles multiple classes in a single model

## Question 2
**For a one-vs-one approach, if there are five classes, how many binary models should be built for binary classifiers?**

1. 10
2. 6
3. 4
4. 5

**Correct Answer: 1**

**Explanation:** For one-vs-one (OvO) with n classes, the number of binary classifiers needed is: n(n-1)/2
With 5 classes: 5(5-1)/2 = 5(4)/2 = 10 classifiers
This creates a binary classifier for every possible pair of classes.

## Question 3
**What is the key advantage of the multinomial model over one-vs-one and one-vs-rest for multiclass classification?**

1. Multinomial is computationally efficient due to its pairwise approach
2. Multinomial requires more classifiers
3. Multinomials work with balanced data
4. Multinomial considers class correlations

**Correct Answer: 4**

**Explanation:** Multinomial models have the key advantage of considering class correlations by modeling all classes simultaneously in a single model. This is in contrast to OvO and OvR approaches which treat classes independently. This allows multinomial models to:
- Capture relationships between different classes
- Make more informed decisions by considering the full probability distribution
- Avoid the potential inconsistencies that can arise from combining multiple binary classifiers
