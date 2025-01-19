# Optimization and Convexity Quiz

## Question 1 (1 pt)
What is the relationship between gradient descent and convexity?

**Options:**
1. Gradient descent is only applicable to non-convex functions
2. Gradient descent can find the global minimum for any type of function, convex or not
3. Gradient descent is guaranteed to find the global minimum only for convex functions
4. Convexity has no effect on the performance of gradient descent

**Answer:** Option 3 - Gradient descent is guaranteed to find the global minimum only for convex functions. This is because in convex functions, there is only one minimum (global minimum), and the gradient always points in the direction of steepest descent towards this minimum.

---

## Question 2 (1 pt)
What is the significance of convexity in optimization problems?

**Options:**
1. Convexity guarantees that the objective function is continuous
2. Convexity ensures that the optimization problem is always feasible
3. Convexity indicates that the problem has multiple optimal solutions
4. Convexity ensures that any local minimum is also a global minimum

**Answer:** Option 4 - Convexity ensures that any local minimum is also a global minimum. This is a key property that makes convex optimization problems particularly tractable, as finding a local minimum guarantees we've found the best possible solution.

---

## Question 3 (1 pt)
Under what circumstances is the loss function f said to be convex?

**Options:**
1. If a line is drawn between two points on a curve, all values on the curve must be on or below the line
2. If a line is drawn between two points on a curve, all values on the curve must be on the line
3. If a line is drawn between two points on a curve, all values on the curve must be below the line
4. If a line is drawn between two points on a curve, all values on the curve must be above the line

**Answer:** Option 1 - A function is convex if a line segment drawn between any two points on the curve has all values of the curve on or below the line segment. This is the mathematical definition of convexity and creates the characteristic "bowl" shape that ensures any local minimum must be a global minimum.

---

# Answer Key
1. Option 3 - Gradient descent is guaranteed to find the global minimum only for convex functions
2. Option 4 - Convexity ensures that any local minimum is also a global minimum
3. Option 1 - If a line is drawn between two points on a curve, all values on the curve must be on or below the line