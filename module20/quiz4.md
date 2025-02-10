# Random Forest Quiz

## Question 1 (1 point)
What is the effect of the random forest algorithm on the correlation between trees in a bagged ensemble?

**Options:**
1. It maintains the correlation between trees
2. It increases the correlation between trees
3. It decreases the correlation between trees
4. It eliminates the correlation between trees

**Answer:** Option 3: It decreases the correlation between trees

*Explanation:* Random forests deliberately reduce correlation between trees by using random feature subsets for each split. This is a key improvement over basic bagging, as lower correlation between trees generally leads to better ensemble performance while maintaining the variance reduction benefits of bagging.

---

## Question 2 (1 point)
In scikit-learn, which parameter tells the algorithm to design each split based on a randomly chosen set of two features?

**Options:**
1. max_feature = 2
2. features = 2
3. max_features = 2
4. max.features = 2

**Answer:** Option 3: max_features = 2

*Explanation:* In scikit-learn's RandomForestClassifier, the max_features parameter controls how many features to consider when looking for the best split. Setting max_features = 2 will restrict each split decision to consider only 2 randomly selected features.

---

## Question 3 (1 point)
Which of the following is the correct statement for importing the random forest classifier from scikit-learn?

**Options:**
1. from sklearn.ensemble import RandomForestClassifier
2. from sklearn import RandomForestClassifier
3. from ensemble import RandomForestClassifier
4. from sklearnensemble import RandomForestClassifier

**Answer:** Option 1: from sklearn.ensemble import RandomForestClassifier

*Explanation:* The RandomForestClassifier is part of scikit-learn's ensemble module, which contains all ensemble learning methods. The correct import statement follows sklearn's standard module organization pattern where related algorithms are grouped into submodules.

---

## Question 4 (1 point)
What is the use of the parameter n_estimators in the RandomForestClassifier() function?

**Options:**
1. It determines the number of trees in the random forest ensemble
2. It specifies the number of features to consider for each split in the trees
3. It sets the maximum depth of each tree in the forest
4. It controls the minimum number of samples required to split an internal node

**Answer:** Option 1: It determines the number of trees in the random forest ensemble

*Explanation:* n_estimators is a fundamental parameter that controls how many decision trees will be created in the random forest. Each tree is trained on a bootstrap sample of the data with random feature selection at each split.

---

## Answer Key

1. Option 3 - Decreases correlation between trees (Key feature of random forests that improves upon basic bagging)
2. Option 3 - max_features = 2 (Correct sklearn parameter name and syntax)
3. Option 1 - from sklearn.ensemble import RandomForestClassifier (Standard sklearn module organization)
4. Option 1 - Number of trees in ensemble (Basic but critical hyperparameter)
