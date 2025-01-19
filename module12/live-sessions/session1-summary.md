# Module 12 - Live Session 1 Summary: Classification Models & KNN

## Classification Performance Metrics

### Key Concepts
- Classification models predict categorical outcomes (unlike regression which predicts numerical values)
- Performance metrics help evaluate how well classification models perform
- Different metrics are suitable for different use cases and industries

### Main Performance Metrics

1. **Accuracy**
   - Most intuitive metric: number of correct predictions / total predictions
   - Limitation: Can be misleading with imbalanced datasets
   - Example: 90% accuracy in fraud detection might mean model just predicts "not fraud" for everything

2. **Precision**
   - Formula: True Positives / (True Positives + False Positives)
   - Measures ability to find only relevant cases
   - Important when false positives are costly
   - Example Use Case: Medical diagnosis where treatment has serious side effects

3. **Recall**
   - Formula: True Positives / (True Positives + False Negatives)
   - Measures ability to find all relevant cases
   - Important when false negatives are costly
   - Example Use Case: Cybersecurity malware detection

4. **F1 Score**
   - Balanced measure between precision and recall
   - Use when you need balance between precision and recall
   - Formula: 2 * (Precision * Recall) / (Precision + Recall)

### Confusion Matrix
- Visual tool to evaluate classification performance
- Shows True Positives, True Negatives, False Positives, False Negatives
- Helps calculate various performance metrics
- Ideal case: High numbers on diagonal (correct predictions)

## K-Nearest Neighbors (KNN)

### Overview
- Non-parametric supervised learning algorithm
- Can be used for both classification and regression
- Works by finding K nearest neighbors to make predictions
- Simple and intuitive algorithm

### How KNN Works
1. Define number of neighbors (K)
2. Calculate distance to all other points
3. Find K closest neighbors
4. Make prediction based on majority vote (classification) or average (regression)

### Advantages
- Simple to understand and explain
- No training phase needed
- Works well with irregular decision boundaries
- Versatile (works for both classification and regression)

### Disadvantages
- Must store all training data
- Slow with large datasets
- Sensitive to irrelevant features
- Requires feature scaling/normalization
- Not as powerful as other modern methods

### Best Practices
- Choose odd values for K to avoid ties
- Normalize/standardize features
- Use cross-validation to select optimal K
- Consider computational resources with large datasets

### When to Use KNN
- Few features (columns)
- Many instances (rows)
- When data doesn't follow clear mathematical pattern
- When quick model updates are needed
- When data storage and query are not issues

## Implementation Tips
- Always split data into training and test sets
- Normalize features before using KNN
- Use cross-validation to find optimal K
- Consider computational resources
- Compare with other models before final selection