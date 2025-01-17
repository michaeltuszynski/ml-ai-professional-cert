# Mini-Lesson 6.1: SVD and PCA

## Types of Machine Learning
As you learned in Module 1, machine learning (ML) is broadly classified into three types:

1. **Supervised Learning**: The algorithm is trained on a labeled dataset, where each input is paired with the correct output. The aim is for the algorithm to learn the mapping from inputs to outputs so that it can predict the output for new inputs.

2. **Unsupervised Learning**: Involves training the algorithm on unlabeled data, where the algorithm must find patterns or structures in the data on its own. Unlike supervised learning, there are no explicit correct outputs, so the algorithm must learn the inherent structure of the data.

3. **Reinforcement Learning**: Training agents to make sequences of decisions in an environment to maximize some notion of cumulative reward. The agent learns by interacting with the environment, receiving feedback in the form of rewards or penalties, and adjusting its strategy to maximize rewards over time.

## SVD and PCA in Unsupervised Learning
In unsupervised learning, singular value decomposition (SVD) and PCA are powerful tools used for extracting important features and reducing the dimensionality of high-dimensional datasets.

### Singular Value Decomposition (SVD)
SVD is a matrix factorization technique used to decompose a matrix into three other matrices. It has various applications, including:
- Data compression
- Noise reduction
- Dimensionality reduction

### Principal Component Analysis (PCA)
PCA is a statistical technique used for dimensionality reduction. It aims to find the directions (principal components) in which the data varies the most. These directions are identified by finding the eigenvectors of the covariance matrix of the data. The principal components are sorted by the amount of variance they explain in the data, allowing for dimensionality reduction by selecting only the most important components.

## Relationship Between SVD and PCA
PCA can be viewed as a specific application of SVD. Given a dataset represented by a matrix 𝑋 with 𝑛 observations and 𝑝 features, PCA seeks to find the eigenvectors of the covariance matrix of 𝑋.