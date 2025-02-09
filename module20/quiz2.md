# Ensemble Learning Quiz

## Question 1 (1 point)
In ensemble learning, the training data is NOT trained on a single model. What does this imply?

**Options:**
1. The training data is used to create multiple models, each trained on different subsets or variations of the data.
2. The training data is used to train a single model that is then used to make multiple predictions on the same data.
3. The training data is used to create a single model that is re-trained multiple times on the same data.
4. The training data is split into multiple sets, and each set is used to train a different model sequentially.

**Answer:** Option 1: The training data is used to create multiple models, each trained on different subsets or variations of the data.

*Explanation:* The core principle of ensemble learning is training multiple distinct models on different aspects of the training data. This allows the ensemble to capture different patterns and perspectives, leading to more robust predictions. Unlike single model approaches, ensemble learning leverages the diversity of multiple models to improve overall performance.

---

## Question 2 (1 point)
In the aggregation step of the metamodel, what is hard voting?

**Options:**
1. The selection of a prediction based on the average of the predictions from all models
2. The selection of a prediction based on the highest probability assigned to each class
3. The selection of a prediction based on the class that receives the most votes
4. The selection of a prediction based on the weighted average of predictions from each model

**Answer:** Option 3: The selection of a prediction based on the class that receives the most votes.

*Explanation:* Hard voting is the most basic form of ensemble prediction aggregation for classification tasks. It simply counts the predictions from each model and selects the class with the most votes (majority vote). This differs from soft voting, which considers prediction probabilities.

---

## Question 3 (1 point)
In ensemble learning for regression problems, how is the output of the models combined?

**Options:**
1. By simple averaging of the predictions from all models
2. By selecting the prediction of the model with the highest accuracy
3. By using a weighted sum of the predictions based on model performance
4. By taking the maximum prediction value among all models

**Answer:** Option 1: By simple averaging of the predictions from all models.

*Explanation:* In basic regression ensembles, predictions are typically combined through simple averaging. While weighted averaging (Option 3) is also valid and commonly used in more sophisticated approaches, simple averaging is the fundamental method for combining regression predictions in ensemble models.

---

## Question 4 (1 point)
What function in Python is used for majority vote?

**Options:**
1. Median()
2. Mean()
3. Mode()
4. Vote()

**Answer:** Option 3: Mode()

*Explanation:* In Python, the Mode() function is used to find the most frequent value in a set, making it the appropriate function for implementing majority voting. This is an implementation detail specific to Python, where mode() from statistics or scipy.stats is commonly used for finding the majority vote.

---

## Answer Key
1. Option 1 - Multiple models on different data subsets (Core principle of ensemble learning)
2. Option 3 - Class with most votes (Definition of hard voting in metamodels)
3. Option 1 - Simple averaging (Basic method for combining regression predictions)
4. Option 3 - Mode() (Python implementation for majority voting)
