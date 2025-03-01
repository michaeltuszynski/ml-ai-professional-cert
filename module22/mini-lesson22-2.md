# Mini-Lesson 22.2: Tricks of the Trade and A/B Testing

Researchers learn how to effectively use neural networks through experience and shared knowledge. However, newcomers often struggle with slow training and poor performance because they're unaware of the helpful techniques that experienced practitioners have learned to use. This mini-lesson will introduce some useful strategies for building high-performance neural networks.

## Shuffling the Examples

Neural networks learn best from diverse examples. It's helpful to select samples that are different from each other during training. This is especially important in stochastic learning, where the order of input doesn't matter. A simple way to implement this is to use examples from different classes consecutively, as similar examples may not provide new information.

## Early Stopping

Early stopping is a regularization technique that helps improve how well a neural network performs on new data. You do this by using a validation set, which is separate from the training set. As you train, you monitor the errors on this validation set. Initially, errors decrease for both sets, but eventually, the validation error will start to increase, while training errors keep decreasing. The goal is to stop training when the validation error is at its lowest point, which indicates the best-performing model.

## Handling Class Imbalance

In classification tasks, problems can arise if some classes have many more examples than others. This imbalance can make it difficult for the network to learn the rarer classes. A simple solution is to adjust the number of examples in each class. You can either:

- Remove some examples from the larger classes (subsampling)
- Duplicate examples from the smaller classes

While subsampling can help, it may also lead to losing useful information.

## Divide and Conquer for Large Tasks

For large-scale problems, a divide-and-conquer approach is effective. This means breaking down complex tasks into smaller, more manageable parts. For instance, in speech recognition, where there are thousands of classes and millions of training samples, using a hierarchical method can simplify the classification process.

Agglomerative clustering is one way to organize large datasets. It groups similar items based on their features, helping to clarify relationships between different classes. When working with large datasets, it's essential to focus on how to train the model effectively and ensure it can adapt to new data, especially in fields such as probability estimation.
