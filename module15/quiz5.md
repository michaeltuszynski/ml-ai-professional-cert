# Gradient Descent and SGD Quiz

## Question 1 (1 point)
What is the primary difference between gradient descent and stochastic gradient descent (SGD)?

**Options:**
1. SGD can only be used for linear models, while gradient descent can be used for any model
2. Gradient descent updates parameters using the entire dataset, while SGD updates using only one sample at a time
3. Gradient descent always converges faster than SGD
4. Gradient descent is more computationally efficient than SGD

**Answer:** Option 2 - Gradient descent updates parameters using the entire dataset, while SGD updates using only one sample at a time. This is the key distinction between the two approaches. SGD trades off computational efficiency for potentially noisier updates by using single samples.

---

## Question 2 (1 point)
Consider the following function call in Python:

```python
mse_gradient_batch_only(theta, batch_indices, X, y_obs)
```

What does the constructor "batch_indices" represent?

**Options:**
1. The list of indices of data to calculate loss
2. The list of indices of data not to include in loss
3. Alpha
4. The size of datasets

**Answer:** Option 1 - The batch_indices parameter represents the list of indices of data points to be used for calculating the loss. This allows the function to compute gradients on a specific subset of the data.

---

## Question 3 (1 point)
Which of the following divides the entire dataset into a batch of datasets in order to save computing time?

**Options:**
1. Alpha
2. Linear regression
3. Stochastic gradient descent
4. Gradient descent

**Answer:** Option 3 - Stochastic gradient descent (SGD) is the technique that divides the dataset into smaller batches to improve computational efficiency while still maintaining the ability to learn from the data.

---

# Answer Key
1. Option 2 - Gradient descent vs SGD parameter updates
2. Option 1 - batch_indices represents data indices for loss calculation
3. Option 3 - SGD divides dataset into batches