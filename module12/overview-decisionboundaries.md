# Overview: Decision Boundaries

To train a classifier on a dataset, you must define a set of hyperplanes. These hyperplanes are called decision boundaries, and they separate the data points into specific classes where the algorithm switches from one class to the next. A data point is more likely to be classified as class A on one side of a boundary and class B on the other.

In the logistic regression example below, a decision boundary is a straight line that separates class A from class B. However, it is difficult in linear models to determine the exact boundary line separating the two classes, so points from class A have also come into the region of class B.

Visualizing decision boundaries in this manner helps demonstrate how sensitive models are to the specific dataset, which can help understand how particular algorithms work and what their limitations are.

![Decision boundaries visualization](<images/bh-pcmlai 12.3.png>)