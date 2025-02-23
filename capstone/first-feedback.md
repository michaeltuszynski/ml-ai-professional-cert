Hi Mike,

Great start to your capstone project!

Here's my feedback:
• While you didn't need it for this submission, for the final submission we expect you to have cross-validation and hyperparameter tuning.
• ROC AUC (0.696) suggests the model is only slightly better than random guessing. Precision for the falls class (0.20) is quite low, meaning a lot of people are falsely classified as high risk, which is not ideal. Here are some ideas to try to get those numbers up:
    - Experiment with non-linear models (Random Forest, XGBoost, LightGBM) which may capture complex relationships better.
    - Use SMOTE for better handling of class imbalance.
    - Hyperparameter tuning should also help.
    - Consider more feature engineering: For example interactions between balance, mobility, and health indicators. Certain medications and conditions increase fall risk. Falls history in previous rounds (Rounds 11-13) can be used as a feature.
• The project does not specify how the model will be used in real-world settings. You should include some clear actionable recommendations. Cost of False Positives vs. False Negatives Not Addressed: In fall prevention, missing a high-risk case (false negative) is worse than flagging a low-risk case.

Hope these recommendations help you for your final submission. Don't hesitate to reach out through the "Support" button on Canvas or book that 1:1 if you want to discuss further :)