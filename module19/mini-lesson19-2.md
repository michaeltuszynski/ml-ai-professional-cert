# Mini-Lesson 19.2: SVD and Funk SVD

Funk SVD is a matrix factorization technique used for collaborative filtering in recommendation systems. Developed by Simon Funk, it is a specific implementation of singular value decomposition (SVD) that is particularly suited for predicting missing entries in user–item rating matrices.

## Key Concepts of Funk SVD:

### Matrix Factorization
Funk SVD decomposes the original user–item rating matrix R into two lower-dimensional matrices: a user matrix and an item matrix, plus a bias term. The goal is to approximate the original matrix R as PQT.

### Model Structure

* **User Matrix (P)**: Each row represents a latent feature vector for a user.
* **Item Matrix (Q)**: Each row represents a latent feature vector for an item.
* **Bias Terms**: Optional biases can be added to account for user and item-specific deviations from the global average rating.

### Objective Function
The method optimizes an objective function that minimizes the difference between the predicted ratings and the actual ratings. This is often done using a loss function such as mean squared error (MSE), and regularization terms are added to avoid overfitting:

$$\text{Objective} = \sum_{(u,i)\epsilon \text{ known ratings} }{(r_{ui}-p_u.q_i^T)^2}+\lambda(\mid p_u \mid^2+\mid q_i \mid^2)$$

Where $r_{ui}$ is the actual rating for user u and item i, $p_u$ and $q_i$ are the latent feature vectors, and $\lambda$ is the regularization parameter.

### Training
The user and item latent factors are initialized randomly and iteratively updated using optimization techniques such as stochastic gradient descent (SGD) to minimize the objective function. This process involves adjusting the latent factors to reduce the error between the predicted and actual ratings.

### Prediction
Once the model is trained, predictions for missing ratings are made by computing the dot product of the user and item latent vectors:

$$\hat{r}_{ui}= p_u.q_i^T$$

This formula provides an estimate of the rating that user u would give to item i based on their latent features.

Funk SVD is a powerful and efficient matrix factorization technique used to build recommendation systems. By decomposing the user–item rating matrix into latent features and minimizing the prediction error, it helps in predicting missing ratings and making personalized recommendations.