# Module 20 Live Session 1 Summary: Ensemble Techniques

## Session Overview
- Topic: Ensemble Techniques in Machine Learning
- Instructor: Viviana Márquez

## Key Topics Covered

### 1. Introduction to Ensemble Learning
- Based on the "wisdom of crowds" concept
- Combines multiple models to make better predictions
- Usually performs better than single predictors
- Can decrease both bias and variance simultaneously
- Particularly effective with tabular data

### 2. Types of Ensemble Methods

#### a. Voting Classifiers
- Combines different types of models (e.g., KNN, Decision Tree, Logistic Regression)
- Uses majority voting (hard voting) or probability averaging (soft voting)
- Less commonly used in industry
- Requires diverse predictors for good results

#### b. Bagging and Pasting
- Uses same type of classifier on different data subsets
- Bagging: sampling with replacement
- Pasting: sampling without replacement
- Bagging more common due to data efficiency

#### c. Boosting
- Sequential learning process
- Each model learns from previous models' mistakes
- Examples: AdaBoost, Gradient Boosting, XGBoost
- Models trained in sequence, not parallel

#### d. Stacking
- Combines multiple models using another model
- Uses a "meta-model" to combine predictions
- More complex implementation

### 3. Random Forest
- Most popular ensemble method
- Combines multiple decision trees
- Uses both data and feature sampling
- Easy to implement compared to other ensemble methods
- Very effective for tabular data
- Trademarked name

### 4. XGBoost
- Extreme Gradient Boosting
- Separate library from scikit-learn
- Often provides best performance for tabular data
- Industry standard for many applications
- Requires separate installation

### 5. Best Practices for Classification Projects
- Always check data balance
- Use SMOTE for imbalanced datasets
- Try ensemble models (industry standard)
- Focus on business interpretation
- Include performance metrics explanation
- Consider model interpretability (e.g., using SHAP)
- Provide clear business recommendations

## Practical Tips
1. Always try ensemble models in real projects
2. Balance datasets when working with classification
3. Connect technical results to business value
4. Include model interpretation when possible
5. Document and explain performance metrics
6. Consider XGBoost or Random Forest for tabular data

## Industry Insights
- Ensemble models (especially XGBoost) are industry standard
- Model interpretation and business value are crucial
- Technical expertise must be balanced with communication skills
- Documentation and explanation of metrics is essential