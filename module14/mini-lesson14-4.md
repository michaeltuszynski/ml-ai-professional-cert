# Mini-Lesson 14.4: Tree Building Parameters

Decision trees are structured like flowcharts where each question helps to separate data in further steps. As shown in the figure below, decision trees can have varying levels and nodes that allow you to visually show the best decision based on input parameters. Familiarize yourself with these basic definitions before moving on.

![alt text](<images/bh-pcmlai 14.3.png>)

The elements of a decision tree are as follows:

- **Root node**: The node that is considered the beginning of the tree
- **Internal node**: The node that can be split into further nodes
- **Leaf node**: The final node that will no longer be split
- **Branch**: The link between nodes

Tuning the hyperparameters of a decision tree is a crucial step in ensuring that your model is as accurate as possible. The following section discusses some of the various hyperparameters provided by scikit-learn for a decision tree and explains how they apply to and impact a decision tree.

A `DecisionTreeClassifier()` is the primary function for implementing a decision tree algorithm. This function allows for input parameters that are critical to an accurate model. These input parameters are defined below.

## Criterion
The criterion measures a split's quality. Scikit-Learn supports Gini criteria for the Gini index and entropy for information gain. It takes the Gini value as a default.

## Robustness
Such a model is robust to variations in the data and does not rely on specific patterns unique to the training dataset.

## Splitter
The splitter specifies the strategy for choosing the split at each node and supports the 'best' value for selecting the best split and 'random' for selecting the best random split. The default value is 'best.'

## max_features
The max_features hyperparameter specifies the number of features to consider when looking for the best and accepts integer, float, string, and None values. This hyperparameter interacts with integers, floats, strings, and 'None' values in the following ways:

- When an integer has been input, that value is used as the maximum features for each split.
- When float is taken, then it shows the percentage of features at each split.
- When auto or sqrt is taken, then max_features = sqrt(n_features).
- When log2 is taken, max_features = log2(n_features).
- When None is taken, max_features = n_features. None is the default value.

## max_depth
The max_depth hyperparameter indicates the maximum depth of the tree. The parameter can either be an integer or None. When None is specified, then the nodes are expanded to the point where all leaves are pure or where all leaves contain fewer samples than min_samples_split. The default value is None.

## min_samples_split
The min_samples_split hyperparameter indicates the minimum number of samples necessary to split an internal node. The minimum number of samples is taken from min_samples_split if it is an integer. If it is a float, the percentage is shown. The default value is 2.

## min_samples_leaf
The min_samples_leaf hyperparameter indicates the minimum number of samples necessary to be at a leaf node. If an integer value is an input, then consider min_samples_leaf as the minimum number. A percentage is displayed if the value is a float. The default value is 1.

## min_leaf_nodes
The max_leaf_nodes hyperparameter indicates the maximum number of samples to be a leaf node. If it is None, then there is no limit to the number of leaf nodes. The default value is None.