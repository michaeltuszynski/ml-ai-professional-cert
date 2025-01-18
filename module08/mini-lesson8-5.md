# Mini-Lesson 8.5: Rules of Training, Validation, and Test Sets

## Overview
In machine learning, one of the objectives is to study and build models that can learn from and predict data from inputs. The input data used to create the model is typically divided into training, validation, and testing datasets in proportions such as:
- 60/20/20
- 70/15/15
- 80/10/10

The choice depends on the specific requirements of the task and the size of the dataset.

## Dataset Types

### Training Dataset
The training dataset is the initial data used to train a machine-learning model. It:
- Assists the model in learning how to apply concepts
- Helps produce results
- Includes descriptions of input data and expected output

### Validation Dataset
Once the fitted model has been determined, the observations in the second set of data, called the validation set, are predicted using the fitted model. The validation set is used to evaluate whether a model fits a training set without bias.

### Test Dataset
The test dataset provides an unbiased evaluation of the final model fit on the training dataset. Important notes:
- If unused in training (such as in cross-validation), it's called a holdout dataset
- In two-subset divisions, the test set may be referred to as the validation set

## Optimal Training Steps

1. Divide your data into training, validation, and test sets (recommended 60/20/20 split)
2. Choose a training algorithm and set of parameters
3. Train the model based on the training set
4. Evaluate the model based on the validation set
5. Repeat steps 2-4 with different training parameters and algorithms
6. Choose the best model and train it using the data from the training and validation sets
7. Evaluate this final model using the test data
