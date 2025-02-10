# Mini-Lesson 20.1: Bagging Classifiers and Bagging Regressors

Bagging classifiers and regressors are ensemble meta-estimators that fit the regressor and classifier models to random subsets of the original dataset. A final prediction is created by combining the predictions from each model. In these meta-estimators, randomization is introduced into the model-building process. Finally, the outcomes are aggregated to reach a categorical outcome: the aggregation averages over the iterations for a numerical target variable.

## Bagging Classifiers

Bagging classifiers aggregate the individual predictions of base classifiers on a random subset of the original dataset (either by voting or by averaging) to form a final prediction. An ensemble of this type of meta-estimator can be calculated by introducing randomization into the construction procedure of a black-box estimator and then reducing its variance.

In the image below, the training data is split into three bootstrapped samples. Each sample is sent to a separate algorithm. The output of each algorithm is then fed to its own classifier. The results of each of the classifiers are then aggregated to arrive at a final prediction.

![A horizontal flowchart illustrating the bagging process](<images/BH-PCMLAI R2_Image recreations.jpg>)

## Bagging Regressors

Bagging regressors are similar to bagging classifiers. Each regressor model is trained on a random subset of the original training set, and the predictions are aggregated. Since the target variable is numeric, the aggregation averages over iterations.

![A flowchart showing aggregation of datasets](<images/BH-PCMLAI R2_Image recreations1.jpg>)