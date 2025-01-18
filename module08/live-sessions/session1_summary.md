# Module 8 - Live Session 1 Summary

## Main Topics Covered
- Linear Regression Review
- Train/Test/Validation Data Sets
- Bias-Variance Trade-off
- Model Performance Metrics
- Feature Engineering Overview

## Linear Regression
- Foundation of machine learning and building block for more complex models
- Interpretable model - coefficients have clear meaning
- Used for regression tasks (predicting numerical values)
- Forms basis for neural networks when combined with activation functions
- Lower bound on performance but preferred when relationships are linear due to interpretability

## Train/Test/Validation Data Split
- Must split data before any feature engineering or modeling
- Typical split: 80% training, 10% validation, 10% test (ratios can vary)
- Training set: Used to train the model
- Validation set: Used for hyperparameter tuning (covered later)
- Test set: Sacred set only used at the end to evaluate final model performance
- Sets must be mutually exclusive to avoid data leakage

## Model Methods in scikit-learn
- `fit()`: Learns parameters from training data
- `transform()`: Applies learned parameters to transform data
- `fit_transform()`: Combines fit and transform in one step
- Only use fit/fit_transform on training data, never on validation/test

## Bias-Variance Trade-off
### Bias
- Error rate on training set
- High bias = underfitting
- Model too simple, not capturing patterns
- Decrease bias by making model more complex

### Variance
- How much model changes with different training data
- High variance = overfitting
- Model too complex, memorizing training data
- Decrease variance by making model simpler

### Trade-off
- Can't minimize both simultaneously
- Decreasing one typically increases the other
- Need to find optimal balance
- Cross-validation helps find sweet spot

## Performance Metrics for Regression
- Root Mean Square Error (RMSE)
  - Measures error magnitude in original units
  - Want as close to 0 as possible
  - Interpretation depends on scale of target variable

- R-squared (Coefficient of Determination)
  - Measures how well model explains variability
  - Range 0-1, want close to 1
  - Below 0.5 is poor performance
  - Negative values indicate very poor model

## Feature Engineering
- Must be done after train/test split
- Required for categorical variables (models only understand numbers)
- Recommended for numerical variables to standardize scales
- Common techniques:
  - One-hot encoding
  - Ordinal encoding
  - Standardization/normalization

## Best Practices
- Always split data before feature engineering
- Never use fit/fit_transform on test data
- Use multiple performance metrics
- Provide business interpretations of model results
- Document objectives and methodology
- Make actionable recommendations based on results

## Interview Tips
- Bias-variance trade-off is common interview topic
- Know how to explain model performance metrics
- Understand when to use different types of encoding
- Be able to interpret model coefficients
- Know how to explain underfitting vs overfitting