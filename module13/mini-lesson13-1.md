# Mini-Lesson 13.1: How to Choose a Method

In machine learning, **binary classification** refers to classifying cases into one of two classes. Comparatively, **multinomial** (or **multiclass**) classification refers to classifying instances into one or more than two classes. Although some classification algorithms naturally support multiple classes, others are binary algorithms by nature. Nevertheless, these algorithms can be turned into multinomial classifiers using various strategies—namely, "one-vs-rest" and "one-vs-one."

## One-vs-Rest (OvR)

One-vs-rest (or one-vs-all) involves breaking down a multiclass dataset into multiple binary classification problems. Each binary classification problem is trained using a binary classifier, and predictions are made using the most accurate model.

Consider the following example featuring a multiclass classification problem with examples for each class: orange, red, and yellow. These could be subdivided into three binary classification datasets as follows:

- Classification Problem 1: red vs. [orange, yellow]
- Classification Problem 2: orange vs. [red, yellow]
- Classification Problem 3: yellow vs. [red, orange]

## One-vs-One (OvO)

Like one-vs-rest, one-vs-one breaks down a multiclass dataset into multiple binary classification problems. However, instead of dividing the dataset into one binary dataset per class, one-vs-one divides the dataset into one dataset per class versus every other class.

Consider the following example featuring a multiclass classification problem with examples for each class: orange, red, and yellow. These could be subdivided into three binary classification datasets as follows:

- Binary classification problem 1: red vs. orange
- Binary classification problem 2: red vs. yellow
- Binary classification problem 3: orange vs. yellow

As you can observe, this strategy differs from the previous one-vs-rest strategy in that there is one class vs. another class as opposed to one class vs. multiple classes.