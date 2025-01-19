# Overview: Classifier Training

The k-nearest neighbors (KNN) method is a supervised machine learning algorithm that is simple and easy to implement for solving classification and regression problems. KNN relies on labeled input data to learn a function that produces an appropriate output when given new unlabeled data. As you can observe in the following plot, KNN has produced a tightly clustered area that identifies similarities in the two datasets.

![KNN Classification Plot](images/bh-pcmlai%2012.2.png)

To accomplish classification tasks, the KNN algorithm finds the distance between a given data point and k numbers of other points in the dataset that are close to the initial point. The algorithm then votes for the most prevalent category for each individual point.

One of the most critical steps in KNN is ensuring the model's accuracy. This is typically accomplished by selecting the optimal value for k. There is no best practice for choosing this value, but as a general rule, you should choose a number that best fits your model. Selecting a lower value may result in overfitting, while choosing a higher value may require high computational complexity.