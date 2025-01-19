# Quiz 4: Classification Metrics and Thresholds

## Question 1 (1 point)
In a k-nearest neighbors model, what happens when the threshold is increased?

**Options:**
1. Both precision and recall improve
2. Recall improves, precision worsens
3. Both precision and recall worsen
4. Precision improves, recall worsens

**Answer:** Option 4: Precision improves, recall worsens
- Core definition: Threshold increase creates a stricter classification boundary
- When threshold increases, we become more selective in positive predictions:
  - Fewer false positives → higher precision
  - More false negatives → lower recall

---

## Question 2 (1 point)
What is the function that generates precision and recall values for various thresholds for a classifier called?

**Options:**
1. threshold_classifier()
2. precision_recall_curve()
3. precision_recall_threshold()
4. precision_threshold()

**Answer:** Option 2: precision_recall_curve()
- Core definition: Standard scikit-learn function for computing precision-recall pairs for different probability thresholds
- Implementation detail: Returns precision, recall, and threshold values as arrays

---

## Question 3 (1 point)
What is a ROC curve?

**Options:**
1. A plot showing the relationship between true positive rate (TPR) and false positive rate (FPR)
2. A measure of the overall correctness of predictions
3. A visualization of the decision boundary for a classifier
4. A graphical representation of the trade-off between precision and recall

**Answer:** Option 1: A plot showing the relationship between true positive rate (TPR) and false positive rate (FPR)
- Core definition: ROC (Receiver Operating Characteristic) curve plots TPR vs FPR at various thresholds
- Shows the trade-off between sensitivity (TPR) and specificity (1-FPR)

---

## Question 4 (1 point)
The confusion matrix has the following values:

```
TP = 50
FP = 5
FN = 10
TN = 35
```

What is the precision of the given confusion matrix?

**Options:**
1. 0.833
2. 0.85
3. 0.909
4. 0.875

**Answer:** Option 3: 0.909
- Core definition: Precision = TP / (TP + FP)
- Calculation: 50 / (50 + 5) = 50/55 ≈ 0.909

---

## Question 5 (1 point)
In the context of a confusion matrix, if a person has actually defaulted on a loan but the model predicts that they have not defaulted, what is this situation called?

**Options:**
1. TN (True Negative)
2. TP (True Positive)
3. FN (False Negative)
4. FP (False Positive)

**Answer:** Option 3: FN (False Negative)
- Core definition: False Negative occurs when the actual class is positive but predicted as negative
- In this context: Actually defaulted (positive) but predicted as non-default (negative)

---

# Answer Key
1. Option 4 - Precision improves, recall worsens (Trade-off due to stricter threshold)
2. Option 2 - precision_recall_curve() (Standard sklearn function for PR curves)
3. Option 1 - TPR vs FPR plot (Fundamental definition of ROC curve)
4. Option 3 - 0.909 (Calculated as TP/(TP+FP))
5. Option 3 - FN (False Negative) (Actual positive, predicted negative)