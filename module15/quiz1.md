# Gradient Descent Quiz

## Question 1 (1 pt)
What is the purpose of gradient descent?

**Options:**
1. To preprocess data
2. To perform statistical tests
3. To maximize functions
4. To minimize functions

**Answer: 4** - Gradient descent is an optimization algorithm that iteratively moves toward the minimum of a function by following the negative of the gradient.

## Question 2 (1 pt)
Consider the following Python function:

`minimize(arbitrary,x0)`

What is the second constructor used as?

**Options:**
1. Zero
2. The starting point for the function to minimize
3. The middle point for the function to minimize
4. The ending point for the function to minimize

**Answer: 2** - In optimization functions, x0 represents the initial point from which the algorithm begins searching for the minimum.

## Question 3 (1 pt)
What is the relationship between the sign of the derivative function and the direction of movement in gradient descent?

**Options:**
1. The sign of the derivative has no effect on the direction of movement.
2. A positive derivative indicates movement toward a minimum.
3. A negative derivative indicates movement toward a maximum.
4. A negative derivative indicates movement toward a minimum.

**Answer: 4** - Gradient descent moves in the opposite direction of the derivative to find minima. When derivative is negative, moving in positive direction leads to minimum.

## Question 4 (1 pt)
In gradient descent, what is the value of the derivative at the point of minima or maxima?

**Options:**
1. Zero
2. Negative
3. Positive
4. Undefined

**Answer: 1** - At any local minimum or maximum, the derivative equals zero as it's a critical point where the slope is flat.

## Question 5 (1 pt)
What is the equation for gradient descent?

**Options:**
1. 𝑥(𝑡+1)=𝑥(𝑡)+(𝛼)𝑑/𝑑𝑥𝑓(𝑥)
2. −𝑥(𝑡+1)=𝑥(𝑡)−(𝛼)𝑑/𝑑𝑥𝑓(𝑥)
3. 𝑥(𝑡)=𝑥(𝑡)−(𝛼)𝑑/𝑑𝑥𝑓(𝑥)
4. 𝑥(𝑡+1)=𝑥(𝑡)−(𝛼)𝑑/𝑑𝑥𝑓(𝑥)

**Answer: 4** - This is the standard gradient descent update equation where we subtract the product of learning rate (α) and derivative to update position.

## Question 6 (1 pt)
What is the relationship between learning rate and overshooting in gradient descent?

**Options:**
1. A higher learning rate can lead to overshooting.
2. A higher learning rate takes more time to converge.
3. The learning rate has no effect on the convergence behavior.
4. A lower learning rate can lead to overshooting.

**Answer: 1** - Large learning rates cause larger steps, potentially jumping over the minimum and leading to overshooting.

---

# Answer Key
1. 4 - To minimize functions
2. 2 - The starting point for the function to minimize
3. 4 - A negative derivative indicates movement toward a minimum
4. 1 - Zero
5. 4 - 𝑥(𝑡+1)=𝑥(𝑡)−(𝛼)𝑑/𝑑𝑥𝑓(𝑥)
6. 1 - A higher learning rate can lead to overshooting