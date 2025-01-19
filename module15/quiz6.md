# Model Complexity and Learning Quiz

## Question 1 (1 point)
What happens when a model is pushed to higher levels of complexity by excessively increasing the number of parameters?

**Options:**
1. The model will necessarily improve its generalization performance on unseen data
2. Increasing complexity guarantees better performance across all datasets
3. The model becomes simpler and requires fewer parameters to fit the data
4. The training error will reduce to zero, but the test error may increase significantly

**Answer:** Option 4 - When a model becomes too complex through excessive parameterization, it tends to overfit the training data. While the training error approaches zero, the model loses its ability to generalize, leading to increased test error.

---

## Question 2 (1 point)
What is a key reason why overparameterized models trained with stochastic gradient descent (SGD) behave similarly to regularized models?

**Options:**
1. The randomness in SGD introduces variability that prevents overfitting
2. They are always guaranteed to find the global minimum during training
3. Overparameterization leads to simpler models that generalize better
4. They require fewer parameters to learn effectively

**Answer:** Option 1 - The stochastic nature of SGD acts as an implicit regularizer. The random sampling of data points introduces noise into the optimization process, which helps prevent the model from overfitting to the training data.

---

## Question 3 (1 point)
How does increasing model complexity generally affect bias and variance in machine learning?

**Options:**
1. Increasing complexity increases both bias and variance
2. Increasing complexity reduces both bias and variance
3. Increasing complexity has no effect on bias or variance
4. Increasing complexity reduces bias but increases variance

**Answer:** Option 4 - As model complexity increases, the model becomes more flexible and can better fit the training data, reducing bias. However, this increased flexibility also makes the model more sensitive to variations in the training data, leading to higher variance.

---

# Answer Key
1. D - Training error reduces to zero, but test error may increase
2. A - Randomness in SGD prevents overfitting
3. D - Increasing complexity reduces bias but increases variance