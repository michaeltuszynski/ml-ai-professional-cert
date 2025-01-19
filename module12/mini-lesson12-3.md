# Mini-Lesson 12.3: Evaluating Classifiers

## Overview: Evaluating Classifiers

Classification performance is measured either by a numeric metric, such as accuracy, or a graphical representation, such as a receiver operating characteristic (ROC) curve. Classification metrics are based on the true positives (TPs), false positives (FPs), false negatives (FNs), and true negatives (TNs) contained in the confusion matrix.

![alt text](<images/bh-pcmlai 12.3.1.png>)

The performance of a model can be evaluated using a variety of metrics. It is critical that you understand what each metric calculates to choose the best evaluation metric for your model. For example, models may be hailed as highly accurate, but depending on the question the model is trying to address, another metric may be more appropriate. The metrics that are typically used to determine the performance of a model are accuracy, precision, recall, and F1. As these measures are often confused and interchanged, this mini-lesson will clarify the differences between them.

## Accuracy

Accuracy is the most intuitive measure of performance, as it is simply the ratio of correctly predicted observations to total observations. Accuracy can be deceiving in that it may signal a highly accurate model, but in all actuality, it has some weaknesses. Accuracy is only useful when the dataset is perfectly symmetrical, where values of FNs and FPs are almost identical, with similar costs. Accuracy is useful in cases where you have balanced classes, which implies that equal importance is given to both the positive and negative classes. Accuracy provides an overall view of the model's performance.

## Precision

Precision is the proportion of accurately predicted positive observations in relation to the total predicted positive observations. High precision is directly correlated to a low FP rate.

Precision is a metric that evaluates the reliability of positive predictions made by a model. It answers the question: "Of all the instances predicted as positive, how many were actually positive?". It is calculated as:

**Precision = TPs / (FPs + TPs​)**

Precision helps in avoiding FPs, also known as type I errors. FPs occur when the model predicts positive (e.g., disease) when the actual class is negative (e.g., healthy). In critical scenarios (e.g., medical diagnosis, fraud detection), FPs can have severe consequences. High precision minimizes false alarms and ensures that positive predictions are trustworthy. Precision becomes crucial when classes are imbalanced. It helps prevent the overestimation of positive cases. It shares an inverse relationship with recall. Increasing precision often leads to lower recall (and vice versa). Finding the right balance depends on the specific problem.

Precision matters when diagnosing a rare disease. An FP (predicting disease when the patient is healthy) can cause unnecessary stress and additional tests. Similarly, in the case of email spam detection, high precision ensures that legitimate emails are not incorrectly marked as spam. In the case of credit risk assessment, precision is crucial to avoid approving risky loans.

## Recall

Recall (a.k.a. sensitivity) is the proportion of correctly predicted positive observations in relation to all of the observations in an actual class. As a result, recall measures the precision with which a model can determine the relevant data.

Recall measures the proportion of actual positive instances (TPs) that the model correctly identifies. It answers the question: "Of all the actual positive cases, how many did the model capture?" It is calculated as:

**Recall = TPs / (TPs + FNs)**

This metric plays a crucial role in areas such as medical diagnosis and quality control. When identifying diseases, missing a TP can have severe consequences. Recall ensures that the actual positive cases are not overlooked. In quality control, for detecting defects or anomalies, recall helps identify all faulty products, minimizing FNs. Recall emphasizes the ability to find actual positive instances. Recall is crucial when avoiding FNs is a priority.

Balancing precision and recall is crucial in scenarios where both FPs and FNs have significant consequences. Please see the table below for more information on the importance of balancing precision and recall in different scenarios.

### Balancing Precision and Recall in Different Scenarios

| Scenario | Precision | Recall |
|----------|-----------|--------|
| Medical Diagnosis | High precision ensures reliable positive predictions (minimizing false alarms). | High recall ensures that actual positive cases are not missed (minimizing FNs). |
| Fraud Detection | High precision avoids unnecessary investigations. | High recall ensures that actual fraud cases are detected. |
| Information Retrieval | High precision ensures that the retrieved results are relevant. | High recall ensures that no relevant documents are missed. |
| Quality Control | High precision avoids false alarms. | High recall ensures that all faulty products are identified. |

## F1 Score

F1 is the weighted average of both precision and recall. The F1 score is essential because it balances precision and recall, providing a single metric that considers both FPs and FNs. It provides a holistic view of model performance, especially in scenarios where precision and recall need careful consideration.

## Model Performance Metrics

| Metric | When to Use | Formula | Example |
|--------|-------------|---------|----------|
| Accuracy | Used when you have a perfectly symmetrical dataset | (TP + TN) ÷ (TP + FP + FN + TN) | One out of every ten labels is incorrect, and nine are correct. Therefore, the accuracy is 0.90. |
| Precision | Used when you want to be more confident of your TPs | TP ÷ (TP + FP) | Two out of every ten cancer samples labeled by your program are healthy, and eight are cancerous. Therefore, the precision is 0.80. |
| Recall | Used when the idea of FPs is far better than FNs | TP ÷ (TP + FN) | Three out of every ten COVID-19 patients are mislabeled by your program as negative, and seven are labeled as positive. Therefore, the recall is 0.70. |
| F1 | Used when you have uneven class distribution | 2 × (recall × precision) ÷ (recall + precision) | Out of every ten people, four are mislabeled as having COVID-19 while healthy, four are correctly labeled as healthy, and two are mislabeled as healthy while having COVID-19. Therefore, the F1 is 0.57. |
