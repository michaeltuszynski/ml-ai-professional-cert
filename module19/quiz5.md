# Quiz 5: Matrix Factorization and Recommendation Systems

## Question 1 (1 point)
Which of the following statements is true regarding scikit-learn and the Funk SVD matrix decomposition algorithm?

**Options:**
1. Scikit-learn supports Funk SVD through a dedicated class for matrix factorization
2. Scikit-learn supports Funk SVD indirectly by implementing it as part of a larger ensemble method
3. Scikit-learn does not support the Funk SVD matrix decomposition algorithm
4. Scikit-learn supports the Funk SVD matrix decomposition algorithm directly

**Answer:** Option 3: Scikit-learn does not support the Funk SVD matrix decomposition algorithm

Explanation: Scikit-learn provides general matrix factorization methods like NMF (Non-negative Matrix Factorization) and TruncatedSVD, but does not implement the specific Funk SVD algorithm. Funk SVD is primarily implemented in specialized recommendation system libraries like Surprise.

## Question 2 (1 point)
In the surprise.SVD() function, which parameter is used to specify the number of latent factors (or factors) for matrix decomposition?

**Options:**
1. n_iter
2. n_factors
3. n_components
4. n_epochs

**Answer:** Option 2: n_factors

Explanation: In the Surprise library's SVD implementation, the parameter 'n_factors' is used to specify the number of latent factors for matrix decomposition. This is distinct from scikit-learn's convention of using 'n_components' or other parameters like 'n_epochs' which control training iterations.

## Question 3 (1 point)
What does the Python statement `model.pu @ model.qi.T` compute in the context of a recommendation system using matrix factorization?

**Options:**
1. The dot product of the user factors and item factors matrices, resulting in a matrix of predicted ratings
2. The sum of the user factors and item factors matrices
3. The dot product of the item factors and user factors matrices, resulting in a matrix of predicted ratings
4. The product of the item factors matrix and its transpose

**Answer:** Option 1: The dot product of the user factors and item factors matrices, resulting in a matrix of predicted ratings

Explanation: The @ operator performs matrix multiplication between the user factors matrix (pu) and the transposed item factors matrix (qi.T). This multiplication reconstructs the ratings matrix, where each element represents a predicted rating for a user-item pair.

---

## Answer Key
1. Option 3 - Scikit-learn does not support Funk SVD (Distinguishes between general matrix factorization and specific Funk SVD implementation)
2. Option 2 - n_factors (Correct parameter name in Surprise library for specifying latent factors)
3. Option 1 - Dot product of user and item factors matrices (Explains matrix multiplication operation for rating prediction)
