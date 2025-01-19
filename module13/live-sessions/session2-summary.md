# Module 13 - Live Session 2 Summary

## Topic: Hotel Booking Cancellation Prediction

This session focused on approaching a classification problem to predict hotel booking cancellations. The instructor walked through a systematic approach to tackle such a machine learning problem.

### Problem Statement
- Predict whether a hotel booking will be cancelled or not
- Dataset contains 56,926 rows and 18 columns (4 categorical, 14 numerical)
- Features include: reservation details, guest information, booking timing, and special requests

### Systematic Approach Discussed

1. **Data Cleaning**
   - Check for null values
   - Verify categorical value consistency
   - Check for wrong data types
   - Remove duplicates
   - Handle outliers

2. **Data Exploration (UBM Framework)**
   - **Univariate Analysis**: Understanding individual columns
   - **Bivariate Analysis**: Relationship between pairs of columns
   - **Multivariate Analysis**: Multiple column relationships
   - Special focus on:
     - Understanding target variable distribution
     - Relationship between target and features
     - Appropriate visualizations (scatter plots, bar plots)

3. **Data Preprocessing**
   - Feature selection
   - Categorical value encoding
   - Numerical feature scaling
   - Optional: Polynomial feature generation

4. **Model Building**
   - Start with dummy classifier (baseline)
   - Implement logistic regression
   - Perform hyperparameter tuning (focus on regularization)

5. **Model Evaluation**
   - Confusion matrix analysis
   - Classification metrics:
     - Accuracy
     - Precision
     - Recall
     - Sensitivity
   - Important consideration: Optimal probability cutoff
     - Based on business impact of false positives vs false negatives
     - Example discussed: Hotel overbooking risks vs lost revenue
     - Consider cost-based indexing for threshold determination

### Key Insights
- The process is iterative, not linear
- May need to revisit previous steps based on model performance
- Business context is crucial for model evaluation
- False positives and false negatives have different business impacts:
  - False Negative: Lost commission from unexpected cancellation
  - False Positive: Risk of overbooking and PR issues

### Best Practices Highlighted
- Always start with a baseline model
- Consider business impact when setting probability thresholds
- Look beyond basic accuracy metrics
- Document correlation analysis during feature exploration
- Maintain balance between model performance and business requirements