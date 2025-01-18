# Module 7 Quiz: Loss Functions

## Question 1 (1 point)
Which of the following statements accurately highlights the difference between MSE and MAE, particularly in their treatment of outliers?

**Options:**
1. MSE computes the logarithm of the absolute difference between prediction and true outcome, while MAE quantifies the percentage difference, leading to divergent behaviors in the presence of outliers.
2. MSE and MAE exhibit similar behaviors in handling outliers and can be used interchangeably in regression tasks.
3. MSE disproportionately penalizes larger errors, making it more sensitive to outliers, whereas MAE treats all errors equally, resulting in greater robustness to outliers.
4. MSE measures the absolute difference between prediction and true outcome, while MAE calculates the mean of the squared differences, resulting in differing sensitivities to outliers.

**Answer:** Option 3: MSE disproportionately penalizes larger errors, making it more sensitive to outliers, whereas MAE treats all errors equally, resulting in greater robustness to outliers.

*Explanation:* The core difference is in how they handle errors: MSE squares the differences (making it more sensitive to outliers), while MAE uses absolute values (treating all errors linearly). MSE gives much higher penalties to outliers as the error increases with the square of the distance, while MAE treats all errors proportionally.

## Question 2 (1 point)
Which of the following loss functions gives higher penalties to outliers?

**Options:**
1. Log-cosh loss
2. L2 loss
3. Huber loss
4. L1 loss

**Answer:** Option 2: L2 loss

*Explanation:* L2 loss (MSE) squares the differences between predicted and actual values, which means it gives disproportionately higher penalties to larger errors (outliers). The squared nature of L2 loss means that as errors get larger, their impact grows quadratically rather than linearly.

## Question 3 (1 point)
When analyzing a graph of a loss function, how can you differentiate between MSE and MAE?

**Options:**
1. Both MSE and MAE have quadratic curves but differ in their steepness.
2. MSE has a quadratic (parabolic) curve, while MAE has a linear (V-shaped) curve.
3. Both MSE and MAE have linear curves but differ in their intercepts.
4. MSE has a linear (V-shaped) curve, while MAE has a quadratic (parabolic) curve.

**Answer:** Option 2: MSE has a quadratic (parabolic) curve, while MAE has a linear (V-shaped) curve.

*Explanation:* MSE produces a smooth, parabolic curve due to its squared terms, while MAE results in a piecewise linear, V-shaped curve. This difference arises from their fundamental definitions: MSE squares the errors leading to smooth curves, while MAE uses absolute values resulting in linear segments.

---

# Answer Key
1. Option 3 (MSE disproportionately penalizes larger errors vs MAE's equal treatment)
2. Option 2 (L2 loss gives highest penalties to outliers)
3. Option 2 (MSE shows quadratic curve vs MAE's linear V-shape)