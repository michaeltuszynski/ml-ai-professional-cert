# Quiz 2

Question 1 (1 pts)
Which of the following statements correctly imports a decision tree model from scikit-learn?
Group of answer choices

from sklearn.tree import DecisionTreeModel

from sklearn.tree import DecisionTree

from sklearn.model import DecisionTreeClassifier

from sklearn.tree import DecisionTreeClassifier

**Correct Answer: 4** - `from sklearn.tree import DecisionTreeClassifier`

**Explanation:**
The correct import statement is `from sklearn.tree import DecisionTreeClassifier`. This is the standard way to import decision tree classifiers in scikit-learn. The other options are incorrect because:
- `DecisionTreeModel` doesn't exist in scikit-learn
- `DecisionTree` is not a valid class name
- `sklearn.model` is not a valid module path (it should be `sklearn.tree`)

Flag question: Question 2
Question 21 pts
Which of the following is not a constructor used in the "tree.plot_tree()" function?
Group of answer choices

rounded

class_names

feature_names

criterion

**Correct Answer: 4** - `criterion`

**Explanation:**
The `plot_tree()` function in scikit-learn's tree module accepts several parameters for visualization, but `criterion` is not one of them. The actual parameters include:
- `rounded` - for rounded edges
- `class_names` - to display class labels
- `feature_names` - to display feature names
`criterion` is actually a parameter used when creating the decision tree, not when plotting it.

Flag question: Question 3
Question 31 pts
Here is a node from a decision tree:

petal_width ≤ 1.75

entropy = 1.0

samples = 100

value = [0, 50, 50]

class = versicolor

Given a single node of a decision tree built with class_names=["a","b","c"], how many samples belong to class "a" at this node?

Group of answer choices

0

50

1.0

100

**Correct Answer: 1** - `0`

**Explanation:**
Looking at the node information, specifically the `value = [0, 50, 50]` array, this represents the sample distribution across the three classes [a, b, c]. The first value (0) corresponds to class "a", indicating there are 0 samples of class "a" at this node. The remaining values show 50 samples each for classes "b" and "c".