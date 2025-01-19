# Quiz 3

## Question 1 (1 pt)
What function can be used to measure the accuracy of a decision tree classifier in Python?

1. f1_score
2. precision_score
3. recall_score
4. accuracy_score

**Correct Answer: 4**

The `accuracy_score` function from scikit-learn is specifically designed to measure the accuracy of classifiers, including decision trees, by calculating the ratio of correct predictions to total predictions.

## Question 2 (1 pt)
What is an impure node in a decision tree?

1. An impure node contains the most common class.
2. An impure node contains training samples from multiple classes.
3. An impure node only contains one class.
4. An impure node contains evenly distributed samples across all classes.

**Correct Answer: 2**

An impure node in a decision tree is one that contains training samples from multiple classes, indicating that the node hasn't perfectly separated the classes yet. Pure nodes, in contrast, contain samples from only one class.