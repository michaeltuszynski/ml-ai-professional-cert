# Module 9: Advanced Model Selection and Regularization

## Video 1: Polynomial Features on Multidimensional Data

### Key Concepts
- Relationship between model complexity, sensitivity, and error
- Extension of polynomial features to multidimensional data
- Impact of increasing polynomial degree on feature generation

### Technical Details
- For 2D input (e.g., horsepower and weight):
  - Degree 2 yields 5 features:
    1. Original features (horsepower, weight)
    2. Squared terms (horsepower², weight²)
    3. Cross terms (horsepower × weight)
  - Degree 3 yields 9 features:
    - Additional cubic terms (horsepower³, weight³)
    - Mixed terms (horsepower² × weight, horsepower × weight²)

### Practical Implications
- Feature space grows rapidly with polynomial degree
- Example: 5 numeric features with degree 3 → 55 dimensional feature set
- Cross-validation becomes computationally expensive
  - 2^55 possible feature combinations
  - ~1 million years to compute all combinations at 1ms per model

### Key Takeaways
- Need for efficient model selection strategies
- Introduction to sequential feature selection and regularization as solutions

## Video 2: Sequential Feature Selection

### Main Concept
- Greedy algorithm for feature selection
- Starts with zero features and incrementally adds best performing ones

### Process
1. Initialize empty selected feature set (φ_selected)
2. For each remaining feature:
   - Fit model with current selected features + candidate
   - Compute development set error
   - Add best performing feature to selected set
3. Repeat until desired number of features reached

### Example
- Starting with 5 features:
  1. First iteration: Test each feature individually
  2. Second iteration: Test remaining features with selected feature
  3. Continue until reaching target feature count

### Implementation Details
- Much faster than exhaustive search
- For 55 features, selecting 4:
  - 214 models total (55 + 54 + 53 + 52)
  - Compared to 2^55 for exhaustive search

### Limitations
- Not guaranteed to find global optimum
- Results may vary with different training/dev splits

## Video 3: Sequential Feature Selection in Scikit-learn

### Implementation
- Uses scikit-learn's built-in functionality
- Requires proper handling of training and development indices
- Results can vary based on random splits

### Best Practices
- Compare model performance across different splits
- Use proper validation techniques
- Consider computational trade-offs

## Video 4: A First Look at Regularization

### Key Concepts
- Alternative to feature selection
- Keeps all features but controls their impact
- Uses alpha parameter for complexity control

### Technical Details
- Ridge Regression basics
- Impact of alpha on model parameters
- Relationship between alpha and model complexity

### Implementation
```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=0.001)
```

### Behavior
- As alpha increases:
  - Parameters get smaller
  - Model becomes less complex
  - Training error increases
  - May improve generalization

## Video 5: How Regularization Works

### Mathematical Foundation
- Objective function = MSE + penalty term
- Ridge regression: penalty = α∑θᵢ²
- Demonstrates trade-off between error and parameter size

### Example Calculation
- Detailed walkthrough of computing:
  - Predictions (ŷ)
  - Mean squared error
  - Penalty term
  - Total objective function

### Key Insights
- Alpha sets "budget" for parameter magnitudes
- Larger alpha forces smaller parameters
- Intercept term not included in penalty

## Video 6: Scaling

### Importance
- Features on different scales affect regularization unequally
- Standardization makes regularization fair across features

### Implementation
```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
```

### Best Practices
- Always scale before regularization
- Use StandardScaler in pipeline
- Keep track of scaling for predictions

## Video 7: Grid Search CV

### Purpose
- Automated hyperparameter tuning
- Systematic model comparison

### Implementation
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'regression__alpha': np.logspace(-5, 4, 100)}
grid_search = GridSearchCV(estimator=pipeline, param_grid=param_grid)
```

### Best Practices
- Define parameter grid carefully
- Use cross-validation
- Access best_estimator_ for final model
- Don't use GridSearchCV directly for predictions

## Video 8: LASSO Regression

### Key Concepts
- L1 regularization
- Penalty term uses absolute values
- Automatic feature selection

### Technical Details
- Penalty term = α∑|θᵢ|
- Forces some parameters exactly to zero
- More computationally intensive than Ridge

### Implementation
```python
from sklearn.linear_model import Lasso
model = Lasso(alpha=1.0)
```

### Use Cases
- When feature selection is desired
- Sparse solution preferred
- Interpretability important

## Video 9: K-fold Cross-Validation

### Process
1. Split data into k folds
2. For each fold:
   - Train on k-1 folds
   - Validate on remaining fold
3. Average results across all folds

### Advantages
- Uses all data for training
- More robust error estimates
- Reduces validation variance

### Implementation
```python
grid_search = GridSearchCV(estimator=pipeline, param_grid=param_grid, cv=5)
```

### Best Practices
- Common k values: 5, 10, or n (leave-one-out)
- Consider computational cost
- Balance between accuracy and speed

## Video 10: Human Resources Applications

### Case Study: Resume Screening
- Goal: Automate applicant screening
- Challenge: Balance quality with diversity

### Approaches
1. Traditional supervised learning
2. Updated LASSO model
3. Upper confidence bound contextual bandit

### Key Findings
- ML models increase hiring yield
- Different impacts on demographic diversity
- Trade-off between exploitation and exploration

### Best Practices
- Consider both performance and fairness
- Use randomized controlled trials for evaluation
- Balance automation with human oversight

## Module Summary

### Key Technologies
- scikit-learn
- StandardScaler
- GridSearchCV
- Ridge and Lasso Regression

### Core Concepts
1. Feature selection vs. regularization
2. L1 and L2 regularization
3. Cross-validation techniques
4. Hyperparameter tuning
5. Model evaluation and selection

### Best Practices
1. Always scale features for regularization
2. Use cross-validation for model selection
3. Consider computational costs
4. Balance model complexity with performance
5. Evaluate models on multiple metrics