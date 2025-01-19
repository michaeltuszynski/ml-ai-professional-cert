# Overview: Support Vector Machines

SVMs work by finding a hyperplane that divides a dataset into two groups. In this dataset, support vectors are the nearest points to the hyperplane—the points that would alter the position of the dividing hyperplane if removed. In this way, they can be regarded as crucial elements of a dataset. If the hyperplane classifies the dataset linearly then it is called as SVC (Support Vector Classifier). If the hyperplane is non-linear then it is Support Vector Machine which uses kernel trick.

## Hyperplane and Classification

As was mentioned previously, the hyperplane is a crucial part of the SVM, as it linearly separates and classifies a dataset. From an intuitive standpoint, the further away the data points are from the hyperplane, the more confident you can be that they are correctly classified. Hence, data points should be as far away from the hyperplane as possible while remaining on the correct side. As a result, new testing data will be assigned to a class based on which side of the hyperplane it lands.

## Advantages and Disadvantages

Here are some of the advantages and disadvantages of SVMs that may be important in your decision-making process:

### Advantages

- SVMs perform well when classes are clearly separated
- SVMs are more effective in high-dimensional spaces
- SVMs are advantageous when the number of dimensions exceeds the number of samples
- SVMs require relatively little memory

### Disadvantages

- The SVM algorithm is not suitable for handling large datasets
- SVMs perform poorly when the dataset has more noise (i.e., if the target classes overlap)
- SVMs use data points placed above and below the classifying hyperplane, so the classification cannot be explained probabilistically
- SVMs require careful selection of the kernel and tuning of hyperparameters, which can be complex and time-consuming