# Module 14 - Live Session 1 Summary: Decision Trees

## Overview
This session focused on decision trees, covering both theoretical concepts and practical implementation. The instructor (Viviana Márquez) provided a comprehensive overview of decision tree algorithms, their mechanics, and their application in machine learning.

## Key Topics Covered

### 1. Introduction to Decision Trees
- Decision trees are non-parametric machine learning models
- Can be used for both classification and regression tasks
- Highly interpretable compared to other models
- Main challenge: prone to overfitting

### 2. Decision Tree Terminology
- Root Node: First node containing entire population
- Splitting: Process of dividing a node into two (typically binary in ML)
- Branch: Connection between nodes
- Decision Node: Node where a question/split occurs
- Leaf Node: Final node containing the prediction
- Pruning: Process of removing branches to prevent overfitting

### 3. Information Gain and Entropy
- Entropy measures the impurity/uncertainty in a node
- For binary classification:
  - Entropy ranges from 0 (pure node) to 1 (maximum impurity)
  - For multi-class problems, entropy can exceed 1
- Information gain measures the reduction in entropy after a split
- Best splits are chosen based on maximum information gain

### 4. Practical Implementation
- Using scikit-learn's DecisionTreeClassifier
- Visualization using graphviz library
- Key parameters:
  - criterion: 'entropy' or 'gini'
  - max_depth: controls tree depth to prevent overfitting
- Importance of hyperparameter tuning

### 5. Best Practices and Tips
- Always try multiple models (not just decision trees)
- Compare with simpler models like logistic regression
- Watch out for overfitting signs:
  - Perfect accuracy (100%) is usually suspicious
  - Nodes with single observations
  - Very deep trees
- Consider using ensemble methods (like Random Forests) for better performance

## Practical Examples
- Demonstrated with Iris dataset
- Showed how to interpret decision tree visualizations
- Covered entropy calculations and information gain computation

## Future Topics
- Random Forests will be covered in later modules
- Ensemble methods can help address decision tree overfitting
- More advanced topics in Module 18 (NLP) for handling text data

## Holiday Break Notice
- Last office hours of the year
- Break starting December 22nd
- Classes resume January 5th