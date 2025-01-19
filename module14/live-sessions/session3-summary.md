# Module 14 - Live Session 3 Summary

## Main Topics Covered
- Decision Trees
- Logistic Regression for Multi-class Classification
- Project Discussion

## Decision Trees Overview

### Key Concepts
- Decision trees can be used for both classification and regression problems
- Works by making decisions at each node to split data
- Uses different metrics for optimization:
  - Entropy (for classification)
  - Gini impurity (for classification)
  - Mean squared error (for regression)

### Advantages
- Easy to interpret through visualization
- Handles both categorical and numerical data
- Fast to train and predict
- Good for smaller datasets with categorical variables

### Disadvantages
- Can easily overfit with large datasets
- Performance may suffer with too many features
- May create complex trees that are hard to interpret

### Best Practices
1. Pruning techniques:
   - Setting max_depth
   - Minimum samples for leaf nodes
   - Minimum samples for splits
2. Use grid search for hyperparameter tuning
3. Cross-validation for better model evaluation
4. Allocate more data for testing due to overfitting risks

## Logistic Regression for Multi-class Problems

### Approaches
1. One-vs-Many
   - Create separate binary models for each class
   - Potential issues with multiple positive predictions
2. Softmax Regression
   - Single model combining all classes
   - Better handling of multiple class probabilities

### Recommendations
- Better suited for binary classification
- Consider other models for multi-class problems
- Works well with simpler datasets and fewer features

## Project Discussion Highlights
- Focus on thought process over model perfection
- Importance of thorough EDA (Exploratory Data Analysis)
- Conduct hypothesis tests to remove inherent biases
- Consider multiple approaches/models for problem-solving
- Image classification projects may benefit from specialized models

## Key Takeaways
1. Choose models based on data characteristics:
   - Dataset size
   - Feature types (categorical vs numerical)
   - Complexity of relationships
2. Always validate model performance through proper metrics
3. Use appropriate pruning techniques to prevent overfitting
4. Consider business context and requirements when selecting models

## Next Steps
- Holiday break announcement
- Students encouraged to continue working on capstone projects
- Focus on data exploration and hypothesis testing