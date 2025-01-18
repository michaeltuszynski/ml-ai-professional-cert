# Mini-Lesson 7.2: Different Types of Loss

To evaluate the effectiveness of a linear regression model, you must first understand loss. The loss function measures the difference between the predicted and actual results. Now you are going to look at some loss functions and how they might be applied to regression.

## Mean Squared Error (MSE)

The MSE is probably the most popular loss function for regression. It is interpreted using the average squared difference between the predicted and actual variables.

### Advantages
- The MSE algorithm can converge to the minimum efficiently with small errors as the gradient slowly declines.

### Drawbacks
- Squared values generally result in a higher training rate
- A very large loss may result in a dramatic jump during backpropagation, which is not desirable
- MSE is sensitive to data outliers
- Data outliers may impact your network more heavily, given the significantly higher loss associated with them

## Root Mean Squared Error (RMSE)

RMSE is a widely used metric for evaluating the performance of a regression model. It measures the square root of the average of squared differences between the predicted and actual values, providing a sense of how well the model's predictions match the observed data.

### Advantages
- Easy to interpret as it's expressed in the same units as the target variable
- Sensitive to larger errors due to the squaring of differences
- Beneficial mathematical properties (continuity and differentiability) for optimization algorithms
- Versatile and reliable metric for evaluating regression models

### Drawbacks
- Sensitive to outliers
- Interpretation challenges with non-normal distributions
- Influenced by data variability, leading to lack of robustness
- Scale variance makes it difficult to compare across different datasets

## Mean Absolute Error (MAE)

The MAE is the simplest method for calculating loss and can be found by taking the average sum of the absolute difference between the actual and the predicted values.

### Advantages
- Effective method due to simplicity
- Computationally inexpensive

### Drawbacks
- Calculates loss by considering all errors on the same scale
- All errors are weighted equally while calculating the mean

## Huber Loss (Smooth MAE)

The Huber loss is a composite of both MSE and MAE that plays a critical role. A higher loss results in the quadratic equation transforming into a linear equation. If the error is smaller than the cut-off (epsilon), MSE is used. Otherwise, MAE is used.

### Advantages
- Outliers are dealt with judiciously
- Local minima do not exist
- Distinguishable at 0, providing stability in optimization

### Drawbacks
- Requires optimization of an additional hyperparameter (epsilon)
- Optimization process is iterative

## Mean Squared Logarithmic Error (MSLE)

MSLE can be used to measure the ratio between the true and predicted values. A regression problem may arise when one wishes to penalize a model too much to predict unscaled quantities. The penalty for huge differences can be minimized by using MSLE.

### Advantages
- Treats small differences between small true and predicted values similarly to large differences between large true and predicted values

### Drawbacks
- Penalizes underpredicted estimates more than overpredicted estimates

## Mean Bias Error (MBE)

Bias is one of the most important topics in machine learning. To prevent overestimation or underestimation, MBE can calculate the model's average bias. It is calculated by taking the actual difference between the target and the predicted value and excluding the absolute difference.

### Advantages
- Can be used to check for bias in a model and rectify it

### Drawbacks
- Not a good measure as positive errors tend to cancel out negative ones
- Can be unreliable as high individual errors may produce low MBE

## Log-Cosh Loss

Log-cosh loss is a smooth loss function used in regression tasks. It combines the best properties of MSE and MAE, offering robustness to outliers while maintaining a smooth gradient.

### Advantages
- Provides smooth gradient and robustness to outliers
- Maintains symmetry
- Ensures uniform treatment of positive and negative errors
- Better generalization and numerical stability

### Drawbacks
- Computationally complex compared to MSE and MAE
- Values are harder to interpret
- Lacks flexibility in adjusting sensitivity to outliers
- May not always outperform simpler loss functions
- Can risk overfitting in noisy datasets

## Loss Function Formulas

| Error Type | Formula |
|------------|---------|
| Mean Squared Error (MSE) | $MSE = \frac{1}{n}\sum(y_i-\hat{y}_i)^2$ |
| Root Mean Squared Error (RMSE) | $RMSE = \sqrt{\frac{1}{n}\sum(y_i-\hat{y}_i)^2}$ |
| Mean Absolute Error (MAE) | $MAE = \frac{1}{n}\sum|y_i-\hat{y}_i|$ |
| Mean Absolute Percentage Error (MAPE) | $MAPE = \frac{100\%}{n}\sum|\frac{y_i-\hat{y}_i}{y_i}|$ |
| Mean Squared Logarithmic Error (MSLE) | $MSLE = \frac{1}{n}\sum(log(y_i+1)-log(\hat{y}_i+1))^2$ |
| Log-Cosh Loss | $L = \sum log(cosh(\hat{y}_i-y_i))$ |