# Mini-Lesson 16.1: Baseline Model and Comparing Classifiers

Baseline classifiers are simple models that you use as reference points to compare the performance of your actual models. They help you understand the minimum performance that your actual models should achieve. You will use baseline classifiers in your next Codio assignment.

## Dummy Classifier

This is a classifier that makes predictions using simple rules, which can be useful as a simple baseline to compare with other (real) classifiers. It is not meant for real-world use, but instead it is used as a reference or a "dummy." The baseline score is the score of accuracy on the test set.

## Support Vector Classifier (SVC)

SVC is a powerful and versatile ML model for both linear and nonlinear classification tasks. In the Python notebook, the wine dataset is used to train an SVC model and compare the performance of different kernels. This is a great way to understand how changing the kernel and tuning the hyperparameters can impact the performance of an SVC.

In SVMs, the kernel function is a critical component that allows the algorithm to fit the maximum-margin hyperplane in a transformed feature space. The choice of kernel is significant because it can greatly influence the performance of the classifier. The different kernel functions used are linear, polynomial, RBF, and sigmoidal. The choice of the best kernel method is not straightforward and often requires empirical testing. Here are some guidelines:

- **Linear Separability**: If your data is linearly separable, you might start with a linear kernel.
- **Problem Complexity**: For more complex problems, where there is no clear margin of separation, a nonlinear kernel such as RBF might be more appropriate.
- **Computational Resources**: Polynomial and RBF kernels can require more computational resources. If you have limitations, you might prefer a linear or sigmoidal kernel.
- **Cross-Validation**: Use cross-validation to compare the performance of different kernels. The kernel that gives the best cross-validation accuracy should be considered.
- **Grid Search**: Perform a grid search with cross-validation to find the optimal parameters for kernel functions, such as degree in the polynomial kernel or RBF kernel.

Ultimately, the best kernel is the one that provides the best performance metrics (such as accuracy, precision, recall, or F1 score) on your validation set while also considering the computational cost and the interpretability of the model. The results can be interpreted on the value of gamma that gave the best result.

### Interpreting Gamma Values

- **High Gamma**: If a high gamma value gives the best performance, it means that the model gives more weight to the training data points that are closer to the decision boundary. This can lead to a more complex model that may capture the training data well but could overfit.
- **Low Gamma**: A low gamma value suggests that the model considers points far from the decision boundary as well. This can lead to a smoother decision boundary and a simpler model that might underfit the data.
- **Cross-Validation Scores**: The best gamma value is one that gives the highest cross-validation score, indicating that the model generalizes well to unseen data. The top-ranked gamma value is typically the best choice.