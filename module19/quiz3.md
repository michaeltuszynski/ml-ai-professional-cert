# Module 19 Quiz 3: Collaborative Filtering and Rating Predictions

## Question 1 (1 point)
What is a notable drawback of the collaborative filtering approach?

**Options:**
1. It depends on user demographic data
2. It always requires explicit item features
3. It requires running through all of the item and user factors
4. It cannot handle large datasets efficiently

**Answer:** Option 3: It requires running through all of the item and user factors

*Explanation:* The core limitation of collaborative filtering is its computational complexity due to the need to process all item and user factors for predictions. This matrix multiplication operation becomes increasingly resource-intensive as the number of users and items grows, affecting scalability.

## Question 2 (1 point)
What is the formula for the predicted rating $\hat{r}_{i,j}$ using the item factor matrix and the user factors matrix?

**Options:**
1. $\hat{r}_{i,j} = \text{row}_i(P)$
2. $\hat{r}_{i,j} = \text{row}_i(P) \cdot \text{col}_j(Q)$
3. $\hat{r}_{i,j} = \text{col}_j(Q)$
4. $\hat{r}_{i,j} = \text{col}_j(Q) \cdot \text{row}_i(P)$

**Answer:** Option 2: $\hat{r}_{i,j} = \text{row}_i(P) \cdot \text{col}_j(Q)$

*Explanation:* The predicted rating is calculated as the dot product of the user factor vector (row i of matrix P) and the item factor vector (column j of matrix Q). This multiplication captures the interaction between user preferences and item characteristics.

## Question 3 (1 point)
How is the mean squared error (MSE) computed in a collaborative filtering approach?

**Options:**
1. By calculating the sum of squared differences between the predicted and actual ratings and then averaging them
2. By computing the product of the predicted and actual ratings and then averaging them
3. By averaging the absolute differences between the predicted and actual ratings
4. By summing the differences between the predicted and actual ratings

**Answer:** Option 1: By calculating the sum of squared differences between the predicted and actual ratings and then averaging them

*Explanation:* MSE is defined as the average of squared differences between predicted and actual values. The formula is $MSE = \frac{1}{n}\sum_{i=1}^n(y_i - \hat{y}_i)^2$ where $y_i$ are actual ratings and $\hat{y}_i$ are predicted ratings.

---

## Answer Key
1. Option 3 - It requires running through all of the item and user factors (Computational complexity limitation)
2. Option 2 - $\hat{r}_{i,j} = \text{row}_i(P) \cdot \text{col}_j(Q)$ (Dot product of user and item factors)
3. Option 1 - By calculating the sum of squared differences between the predicted and actual ratings and then averaging them (Standard MSE formula)
