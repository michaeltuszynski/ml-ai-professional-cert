# Quiz 7: Model Evaluation and Testing

## Question 1 (1 point)
In machine learning, the final estimate of outcome is ideally done on a third dataset. What is this third dataset commonly called?

**Options:**
1. Development set
2. Training set
3. Validation set
4. Test set

**Answer:** Option 4: Test set

The test set is a separate dataset used for final model evaluation after all training and validation is complete. It provides an unbiased estimate of model performance on completely unseen data, ensuring we haven't inadvertently overfitted to either the training or validation sets.

---

## Question 2 (1 point)
Consider the following Python code:

```python
diamond_training_data, diamond_validation_data, diamond_test_data = np.split(diamond_data, [1600, 1900])
```

For the datasets of 2400 rows, what would be the size of the Diamond_test_data?

**Options:**
1. 1,900
2. 1,600
3. 400
4. 500

**Answer:** Option 4: 500

The np.split function with indices [1600, 1900] splits the 2400-row dataset into three parts:
- First split at 1600: Training data (1600 rows)
- Second split at 1900: Validation data (300 rows)
- Remaining data: Test data (2400 - 1900 = 500 rows)

---

## Question 3 (1 point)
Why is a test set required in addition to the training and validation datasets when training a machine learning model?

**Options:**
1. To evaluate the final performance of the model on unseen data
2. To tune the hyperparameters of the model during training
3. To create more training data by combining it with the training set
4. To help the model learn the test data and improve its accuracy

**Answer:** Option 1: To evaluate the final performance of the model on unseen data

The test set serves as a final, unbiased evaluation of model performance. It should never be used during training or hyperparameter tuning to ensure we get a true measure of how well our model generalizes to completely new data.

---

## Answer Key
1. Option 4 - Test set (Final evaluation dataset for unbiased performance assessment)
2. Option 4 - 500 (Remaining rows after splits at 1600 and 1900 in 2400-row dataset)
3. Option 1 - Evaluate final performance on unseen data (Essential for unbiased model evaluation)