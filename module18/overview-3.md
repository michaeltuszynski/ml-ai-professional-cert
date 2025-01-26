# Overview: Training Evaluation

Depending on the NLP task, the evaluation metric is essential in measuring the model's performance. When assessing the quality of models in production, you would use business metrics. You can divide evaluation metrics into two categories:

* **Intrinsic evaluation** focuses on intermediate objectives (e.g., the performance of an NLP component on a specific subtask).
* **Extrinsic evaluation** is a review of the performance of the final objective (the component's performance concerning the entire application).

Extrinsic evaluation is critical since stakeholders want to know how well the model solves the business problem. However, the AI team needs to measure its performance using intrinsic evaluation metrics. Here are some intrinsic evaluation metrics that you might consider as a part of your efforts:

* Confusion matrix
* Root mean squared error (RMSE)
* F1 score
* Area under the curve (AUC)
* Perplexity
* Metric for Evaluation of Translation with Explicit ORdering (METEOR)
* Recall-Oriented Understudy for Gisting Evaluation (ROUGE)