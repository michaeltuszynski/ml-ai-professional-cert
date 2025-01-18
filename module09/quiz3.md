# Sequential Feature Selection Quiz

## Question 1 (1 point)
When using sequential feature selection in Python, what are the names of the two sets of indices that the data is divided into?

**Options:**
1. Training and cross-validation indices
2. Training and testing indices
3. Training and development indices
4. Validation and testing indices

**Answer:** Option 2: Training and testing indices

In sequential feature selection, the data is split into training and testing indices. The training set is used to fit the model, while the testing set evaluates the performance of selected features. This is distinct from cross-validation, which involves multiple training-validation splits.

---

## Question 2 (1 point)
When using sequential feature selection on a dataset with 12 features, how many models would you need to fit if you want to select five features?

**Options:**
1. 38
2. 42
3. 50
4. 32

**Answer:** Option 1: 38

For selecting the top four features from 12 features, you need to fit: (12 + 11 + 10 + 9) = 38 models. At each step, you evaluate the remaining features to select the next best one, requiring fewer evaluations as features are selected.

---

## Question 3 (1 point)
Why do sequential feature selection models that are built on the same dataset not return the same features in multiple runs?

**Options:**
1. The dataset is changing over time
2. The features themselves are unstable
3. The models are overfitting to the training data
4. The feature selection process involves randomness

**Answer:** Option 4: The feature selection process involves randomness

The randomness in sequential feature selection comes from the cross-validation splits and initialization of models. This inherent randomness means that different runs may select different features, even on the same dataset.

---

## Answer Key
1. Option 2 - Training and testing indices (Basic split for model fitting and evaluation)
2. Option 1 - 38 models (Sum of evaluations needed: 12+11+10+9)
3. Option 4 - Feature selection process involves randomness (Due to random CV splits and model initialization)