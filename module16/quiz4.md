# Support Vector Machines Quiz

## Question 1 (1 point)
How does the size of the kernel matrix affect training in linear regression using kernels?

**Options:**
1. It improves training accuracy by reducing overfitting
2. It simplifies training by reducing computational complexity
3. It complicates training due to increased computational requirements
4. It has no impact on training efficiency

**Answer:** Option 3

**Explanation:**
Core Definition: The kernel matrix grows quadratically with the number of training examples, as it computes similarities between all pairs of data points.

Implementation Details:
- The kernel matrix has dimensions n×n, where n is the number of training examples
- Computing and storing this matrix becomes computationally expensive for large datasets
- Matrix operations during training become more intensive with larger matrices
- Options 1, 2, and 4 are incorrect because they don't acknowledge the computational burden of large kernel matrices

---

## Question 2 (1 point)
What is a disadvantage of using SVM as a maximum margin classifier?

**Options:**
1. SVM requires a linearly separable dataset for effective classification
2. SVM is computationally efficient only for small datasets
3. SVM is highly sensitive to outliers in the dataset
4. SVM does not perform well with high-dimensional data

**Answer:** Option 3

**Explanation:**
Core Definition: Maximum margin classifiers aim to find the hyperplane that maximizes the distance to the nearest training data points of any class.

Implementation Details:
- Outliers can significantly influence the position of the decision boundary
- Since SVM tries to maximize the margin, outliers can force the boundary to shift substantially
- This sensitivity can lead to suboptimal classification boundaries
- Options 1, 2, and 4 are incorrect because:
  - SVMs can handle non-linearly separable data using kernels
  - SVMs actually perform well with high-dimensional data
  - Computational efficiency is more related to the number of samples than the algorithm itself

---

## Question 3 (1 point)
What is the package you need to import from the Python library "sklearn.svm" to use SVMs?

**Options:**
1. Support Vector
2. ScikitSVM
3. SVM
4. SVC

**Answer:** Option 4

**Explanation:**
Core Definition: SVC (Support Vector Classification) is the main class for support vector classification in scikit-learn.

Implementation Details:
- The correct import statement is: `from sklearn.svm import SVC`
- SVC implements support vector classification for multiple classes
- Options 1-3 are incorrect as they are not actual class names in sklearn.svm
- This naming follows scikit-learn's convention of using clear, specific class names

---

## Question 4 (1 point)
Which of the following is not a constructor to the function "SVC()" when "(kernel = 'poly')"?

**Options:**
1. Degree
2. Gamma
3. Coef
4. Alpha

**Answer:** Option 4

**Explanation:**
Core Definition: The polynomial kernel in SVM has specific parameters that control its behavior.

Implementation Details:
- Valid parameters for polynomial kernel include:
  - degree: Controls the degree of the polynomial
  - gamma: Kernel coefficient
  - coef0: Independent term in the polynomial
- Alpha is not a parameter for SVC with polynomial kernel
- It's often confused with the alpha parameter in other ML algorithms

---

# Answer Key
1. Option 3: Complicates training due to increased computational requirements - Kernel matrix size impacts computation
2. Option 3: SVM is highly sensitive to outliers in the dataset - Affects maximum margin classification
3. Option 4: SVC - Correct package name in sklearn.svm
4. Option 4: Alpha - Not a valid constructor parameter for polynomial kernel SVM