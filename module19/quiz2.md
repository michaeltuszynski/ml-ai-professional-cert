# Quiz 2: Recommendation Systems - User Factors

## Question 1 (1 point)
In terms of recommendation systems, how can the user factors be calculated?

**Options:**
1. Average of item factors
2. Intercept of linear regression
3. Parameters of linear regression
4. Sum of item factors

**Answer:** Option 3: Parameters of linear regression

Explanation: User factors are calculated as the parameters (coefficients) of linear regression models. In collaborative filtering, these parameters represent the user's latent preferences and are learned by minimizing the prediction error across known ratings.

## Question 2 (1 point)
In collaborative filtering, when estimating unknown ratings from users, how does the algorithm initially approach the user factors?

**Options:**
1. By declaring random user factors
2. By applying a default rating for all items
3. By using predefined user factors from a different dataset
4. By setting them to zero

**Answer:** Option 1: By declaring random user factors

Explanation: In collaborative filtering, user factors are typically initialized with random values. This random initialization helps avoid local optima during the optimization process and allows the algorithm to explore different potential solutions during training.

## Question 3 (1 point)
To calculate the user factors for all users from randomly defined item factors, which model is used?

**Options:**
1. SVMs
2. PCA
3. Random guess
4. Linear regression

**Answer:** Option 4: Linear regression

Explanation: Linear regression is used to calculate user factors because it provides a mathematical framework for learning the optimal user factors that minimize the prediction error between estimated and actual ratings, given the item factors.

---

## Answer Key
1. Option 3 - Parameters of linear regression (User factors are learned as regression parameters to minimize rating prediction error)
2. Option 1 - Random initialization (Helps avoid local optima in optimization)
3. Option 4 - Linear regression (Mathematical framework for learning optimal user factors)
