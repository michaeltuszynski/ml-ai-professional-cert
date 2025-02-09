# Module 20: Ensemble Techniques

## Overview
This module covers ensemble learning methods in machine learning, exploring how combining multiple models can improve prediction accuracy and robustness. Key topics include bagging techniques like Random Forests and boosting methods like AdaBoost and Gradient Boosting Trees.

## Video 1: Wisdom of the Crowd

### Key Concepts
- **Ensemble Learning Foundation**:
  - Definition: Combining multiple models to make better predictions
  - Based on principle that collective decisions can outperform individual ones
  - Requires independence between individual decisions
  - Examples: Medical second opinions, parliamentary debate, popular vote

- **Model Types and Components**:
  - Individual models can include KNN, linear regression, logistic regression, decision trees, SVMs
  - Each model acts as predictor/classifier depending on context
  - Models can be combined using various aggregation methods

### Technical Details
- **Statistical Properties**:
  ```
  - Variance reduction through averaging
  - Population unbiasedness leads to crowd wisdom
  - Independence of decisions crucial for effectiveness
  ```

### Practical Applications
- **Medicine**: Seeking second opinions for diagnoses
- **Government**: Parliamentary debate for decision making
- **Democracy**: Popular vote for leadership selection
- **Machine Learning**: Combining multiple models for improved predictions

## Video 2-3: Aggregating Predictors

### Key Concepts
- **Metamodel Architecture**:
  - Splits data into training and testing sets
  - Trains multiple base models
  - Aggregates predictions through voting or averaging
  - Can assign weights to individual models

- **Aggregation Methods**:
  - Classification: Hard voting (majority) or soft voting (probability averaging)
  - Regression: Simple averaging of predictions
  - Optional weighting of individual models (α1 through αm)

### Code Examples
```python
# Basic ensemble implementation
clfs = [
    Pipeline([('scaler', StandardScaler()), ('lr', LogisticRegression())]),
    Pipeline([('scaler', StandardScaler()), ('svc', SVC())]),
    DecisionTreeClassifier(),
    Pipeline([('scaler', StandardScaler()), ('knn', KNeighborsClassifier())])
]

# Train models and make predictions
for clf in clfs:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

# Ensemble prediction through majority vote
ensemble_pred = stats.mode(y_pred)[0]
```

### Best Practices
1. Normalize input data for non-tree models
2. Use pipelines for preprocessing steps
3. Consider model correlation when selecting ensemble members
4. Monitor individual model performance

## Video 4-5: Bootstrapping and Bagging

### Key Concepts
- **Bootstrap Sampling**:
  - Definition: Sampling with replacement from original dataset
  - Creates multiple training sets
  - Approximately 63.2% of original samples in each bootstrap sample
  - Enables out-of-bag evaluation

- **Bagging (Bootstrap Aggregation)**:
  - Reduces model variance
  - Works particularly well with high-variance models
  - Introduces Out-of-Bag (OOB) evaluation
  - Parallel training possible

### Technical Details
- **Mathematical Properties**:
  ```
  P(sample included) = 1 - (1 - 1/N)^N
  Asymptotic inclusion rate ≈ 0.632 (1 - 1/e)
  ```

### Code Examples
```python
# Basic bagging implementation
trees = []
for _ in range(1000):
    # Bootstrap sample
    indices = np.random.choice(len(X_train), len(X_train), replace=True)
    X_bootstrap = X_train[indices]
    y_bootstrap = y_train[indices]

    # Train tree
    tree = DecisionTreeClassifier()
    tree.fit(X_bootstrap, y_bootstrap)
    trees.append(tree)

# Scikit-learn implementation
from sklearn.ensemble import BaggingClassifier
bag_clf = BaggingClassifier(
    base_estimator=DecisionTreeClassifier(),
    n_estimators=100,
    oob_score=True
)
```

### Best Practices
1. Use sufficient number of bootstrap samples
2. Monitor out-of-bag score for model evaluation
3. Consider computational resources vs accuracy tradeoff
4. Use deep trees as base models (low bias, high variance)

## Video 6-7: Random Forests

### Key Concepts
- **Random Forest Improvements**:
  - Further decorrelates trees through feature randomization
  - Uses subset of features for each split (max_features parameter)
  - Combines bagging with random feature selection
  - Provides feature importance measures

- **Feature Importance**:
  - Measures feature contribution to entropy reduction
  - Provides interpretability for the model
  - Helps in feature selection and understanding

### Technical Details
- **Implementation Parameters**:
  ```python
  # Key parameters
  n_estimators: int  # number of trees
  max_features: int or float  # features considered for each split
  max_depth: int  # maximum tree depth
  oob_score: bool  # whether to use out-of-bag samples
  ```

### Code Examples
```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    max_features='sqrt',
    oob_score=True
)
rf.fit(X_train, y_train)

# Feature importance
importances = rf.feature_importances_
```

### Best Practices
1. Choose appropriate number of trees (n_estimators)
2. Consider computational resources vs accuracy tradeoff
3. Use feature importance for model interpretation
4. Monitor out-of-bag score for model evaluation
5. Tune max_features parameter based on problem

## Video 8: AdaBoost

### Key Concepts
- **Adaptive Boosting**:
  - Sequential ensemble method
  - Uses weak learners (usually decision stumps)
  - Adjusts sample weights based on misclassification
  - Slow learner resistant to overfitting

- **Algorithm Components**:
  - Weak classifier selection
  - Influence parameter (α) calculation
  - Sample weight updating
  - Weighted majority voting for final prediction

### Technical Details
- **Key Formulas**:
  ```
  Influence parameter: αs = 1/2 * log((1-εs)/εs)
  Weight updates: w * exp(±αs)
  ```

### Code Examples
```python
from sklearn.ensemble import AdaBoostClassifier

ada = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=100
)
ada.fit(X_train, y_train)
```

### Best Practices
1. Use simple base models (decision stumps)
2. Monitor learning curve to determine iterations
3. Consider early stopping if performance plateaus
4. Balance number of estimators with computational cost

## Video 9: Gradient Boosting Trees

### Key Concepts
- **Gradient Boosting Framework**:
  - Builds model additively
  - Uses gradient descent optimization
  - Can use various loss functions
  - Typically uses deeper trees than AdaBoost

- **Implementation Details**:
  - Sequential training process
  - Learning rate controls step size
  - Number of estimators affects model complexity
  - Residual fitting approach

### Technical Details
- **Algorithm Steps**:
  ```
  1. Initialize model with constant value
  2. Compute residuals
  3. Train weak learner on residuals
  4. Add scaled weak learner to ensemble
  5. Repeat steps 2-4
  ```

### Code Examples
```python
from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=3
)
gbr.fit(X_train, y_train)
```

### Best Practices
1. Control tree depth to manage model complexity
2. Use appropriate learning rate (typically 0.1 or smaller)
3. Monitor validation performance
4. Consider early stopping
5. Balance number of estimators with computational cost

### Practical Applications
- Search engines
- Recommendation systems
- Competition winning solutions
- Industrial applications requiring high accuracy