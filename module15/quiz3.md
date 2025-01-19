# Quiz 3: Gradient Descent and Linear Regression

## Question 1 (1 point)
What is the correct formula for mean squared error?

**Options:**
1. (|y_hat - y_obs|)
2. (y_hat**2 - y_obs**2)
3. sqrt((y_hat - y_obs)**2)
4. ((y_hat - y_obs)**2)

**Answer:** Option 4. The mean squared error (MSE) is calculated as the squared difference between predicted (y_hat) and observed (y_obs) values. This creates a convex loss function suitable for optimization.

---

## Question 2 (1 point)
What is the alternative way of representing the linear equation θ₁+θ₂x in Python?

**Options:**
1. `X@np.array([θ₁,θ₂])`
2. `X@np([θ₁,θ₂])`
3. `X@np.array[θ₁].np.array[θ₂]`
4. `np.array([θ₁,θ₂])@X`

**Answer:** Option 1. Using NumPy's matrix multiplication operator `@`, the correct way to represent θ₁+θ₂x is `X@np.array([θ₁,θ₂])`. This maintains the proper order of multiplication for the input vector and parameter vector.

---

## Question 3 (1 point)
What is the primary purpose of using gradient descent in optimizing a 2D function?

**Options:**
1. To update parameters in a way that reduces the loss function iteratively
2. To find the local minimum of the function by following the negative gradient
3. To move toward the local maximum of the function
4. To make the function more complex and difficult to optimize

**Answer:** Option 2. Gradient descent follows the negative gradient to find the local minimum of the function. It iteratively updates parameters in the direction that reduces the loss function most rapidly.

---

## Question 4 (1 point)
To reduce the loss function, how should the θ values be adjusted?

**Options:**
1. Increase the θ values if the gradient is positive
2. Keep the θ values constant during optimization
3. Adjust the θ values in the direction of the negative gradient
4. Decrease the θ values if the gradient is negative

**Answer:** Option 3. To minimize the loss function, parameters should be adjusted in the direction of the negative gradient. This ensures we move towards the minimum of the loss function.

---

# Answer Key
1. Option 4: ((y_hat - y_obs)**2)
2. Option 1: `X@np.array([θ₁,θ₂])`
3. Option 2: To find the local minimum of the function by following the negative gradient
4. Option 3: Adjust the θ values in the direction of the negative gradient
