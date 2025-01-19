## Live Session 3 Summary - KNN and Model Evaluation

### Main Topics Covered
1. KNN Classification
2. Model Evaluation Metrics
3. ROC and AUC Curves

### KNN Classification Overview
- Demonstrated KNN classification using an IBM employee attrition dataset
- Explained how KNN works with different k values using visual examples
- Default k value in scikit-learn is 5
- Importance of data normalization for KNN (though not implemented in the demo)

### Model Evaluation Deep Dive
#### Confusion Matrix
- Explained using binary classification example (attrition prediction)
- Components: True Positives, True Negatives, False Positives, False Negatives
- Demonstrated how accuracy alone can be misleading (80% accuracy but poor attrition prediction)

#### Key Metrics
1. **Precision**: TP / (TP + FP)
   - Measures accuracy of positive predictions
2. **Recall**: TP / (TP + FN)
   - Measures ability to find all positive cases
3. **F1 Score**: Harmonic mean of precision and recall
   - Provides balanced measure between precision and recall
   - Available for each class in multi-class classification

#### ROC and AUC
- ROC: Receiver Operating Characteristics
- Plots True Positive Rate vs False Positive Rate at various thresholds
- AUC (Area Under Curve):
  - Value between 0 and 1
  - Perfect classifier has AUC = 1
  - Higher values indicate better model performance

### Important Takeaways
1. Don't rely solely on accuracy metrics
2. Consider class imbalance in datasets
3. Choose evaluation metrics based on problem context
4. Trade-offs between false positives and false negatives
5. For multi-class problems:
   - Confusion matrix becomes more complex
   - F1 scores still available for each class

### Practical Tips
1. Start with simpler models and fewer features
2. Consider data balancing techniques
3. Adjust classification thresholds as needed
4. Normalize data for KNN (recommended)
5. Choose odd numbers for k to avoid ties

### Additional Notes
- Capstone project meetings mentioned
- One-on-one sessions available for project discussion
- Emphasis on thorough EDA (Exploratory Data Analysis) before modeling