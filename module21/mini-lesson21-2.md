# Mini-Lesson 21.2: Popular Hyperparameters

## Overview

While an organization may set its own best practices for developing deep learning models, here is a list of some important ones to keep in mind:

- Batch normalization is a technique for standardizing inputs into a network, applied to either the activations of a previous layer or direct inputs
- Residual connection is a skip-connection in which the residual functions are learned with reference to the layer inputs rather than learning unreferenced functions
- Hyperparameter optimization algorithms find the hyperparameter tuple that minimizes a predefined loss function based on independent data
- Ensemble learning reduces the variance of predictions and generalization error by combining predictions from multiple neural network models

With neural networks, there are many hyperparameters, which can be challenging to tune manually. Therefore, KerasTuner is used to make it easy to tune the hyperparameters of neural networks. This is similar to what you have seen in machine learning when using grid search or random search.

Using the KerasTuner, you can choose the right set of parameters for your TensorFlow programs. This is known as hyperparameter tuning or hyper tuning of your machine learning application to select the correct hyperparameters.

In machine learning, hyperparameters determine the model's training process and topology. During the training process, these variables remain constant and directly affect the performance of your machine learning program. There are two types of hyperparameters:

- Model hyperparameters that affect the model selection, such as the number and width of hidden layers
- Algorithm hyperparameters that affect the quality and speed of the learning algorithm, such as the number of neighbors for a k-nearest neighbors classifier and the learning rate for stochastic gradient descent (SGD)

## Popular Hyperparameters

This mini-lesson aims to cover some of the more popular hyperparameters. They include the dropout rate and the regularization parameter.

### Dropout Rate

The technique of dropout involves ignoring randomly selected neurons during training. Instead, they are randomly 'dropped out.' The result is that their contribution to downstream activation is removed in the forward propagation, and their weights are not updated in the backpropagation.

### Regularization Rate

The term 'regularization' refers to a number of techniques that reduce the complexity of a neural network model during training to reduce overfitting. Two prevalent and efficient regularization techniques are L1 and L2.

**L1 Regularization**
L1 regularization penalizes the absolute magnitude of the coefficients, i.e. limits the coefficient size. As a result, L1 can produce sparse models (with few coefficients). Some coefficients can become zero and can be eliminated. Lasso regression uses this technique.

**L2 Regularization**
In L2 regularization, the square of the magnitude of the coefficients is added to the penalty. As a result, the L2 model does not yield sparse models, and all coefficients are shrunk by the same factor (none are eliminated). Regression and support vector machines use this technique.

