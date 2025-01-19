# Support Vector Machines (SVM) - Live Session Summary

## Introduction and Context
- Part of Section 2: Classical Machine Learning
- Focus on tabular data analysis and foundational machine learning concepts
- Builds groundwork for understanding deep learning (Section 3)

## Core Concepts of SVM

### Basic Principles
- SVM is primarily used for classification tasks
- Can handle both binary and multi-class classification
- Works by finding optimal hyperplanes to separate classes
- Default behavior is binary classification

### Key Components
1. **Hyperplane**
   - Line in 2D, plane in 3D, hyperplane in higher dimensions
   - Separates different classes in the feature space
   - Optimal hyperplane maximizes margin between classes

2. **Support Vectors**
   - Data points closest to the hyperplane
   - Define the margin boundaries
   - Critical for determining optimal separation

3. **Margin**
   - Space between hyperplane and nearest data points
   - Goal is to maximize this margin
   - Can be hard or soft depending on data separability

### Kernel Trick
- Transforms non-linearly separable data into higher dimensions
- Makes linear separation possible in transformed space
- Common kernel types:
  - Linear (default)
  - Polynomial
  - RBF (Radial Basis Function)
  - Sigmoid

## Multi-class Classification Strategies

### One-vs-One (OvO)
- Creates binary classifier for each pair of classes
- Number of classifiers = n(n-1)/2 where n is number of classes
- Better for small number of classes
- Default behavior in scikit-learn

### One-vs-All (OvA) / One-vs-Rest (OvR)
- Creates one classifier per class
- Number of classifiers = n (number of classes)
- Better for large number of classes
- Requires explicit implementation in scikit-learn

## Hyperparameters

### C Parameter
- Controls trade-off between margin maximization and classification error
- Higher C: stricter classification, smaller margin
- Lower C: larger margin, more tolerant of errors

### Gamma Parameter
- Defines influence range of each training example
- Affects decision boundary shape
- Only applicable for RBF, polynomial, and sigmoid kernels

## Practical Implementation

### Model Selection
1. Choose appropriate kernel based on data characteristics
2. Use cross-validation for hyperparameter tuning
3. Consider data size and class distribution for OvO vs OvA strategy

### Best Practices
- Scale features before training
- Perform hyperparameter tuning using GridSearchCV
- Save trained models using pickle for deployment
- Validate performance using appropriate metrics

## Advantages and Limitations

### Advantages
- Effective for non-linear classification
- Works well with medium-sized datasets
- Multiple kernel options for different data types
- Good at avoiding overfitting

### Limitations
- Computationally intensive for large datasets
- Sensitive to feature scaling
- Kernel selection can be challenging
- Memory intensive for large datasets

## When to Use SVM
- Medium-sized datasets (hundreds to few thousand samples)
- Binary or multi-class classification problems
- When data is not linearly separable
- When computational resources are sufficient