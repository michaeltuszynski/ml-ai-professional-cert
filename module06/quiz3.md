# K-means Clustering Quiz

## Question 1 (1 point)
In the k-means clustering algorithm, how is inertia defined?

**Options:**
1. Integration of the squared distances from points to their centroids
2. Sum of the squared distances from points to points
3. Sum of the squared distances from points to their centroids
4. Squared distances from points to their centroids

**Answer:** Option 3: Sum of the squared distances from points to their centroids

*Explanation:* Inertia is precisely defined as the sum of squared distances of samples to their closest centroid. This is the core definition used to measure cluster cohesion in k-means. It serves as the objective function that k-means tries to minimize during optimization.

---

## Question 2 (1 point)
What is the stopping criteria for k-means clustering?

**Options:**
1. Assignment step has a change of data points
2. The datapoints assigned to the cluster keeps changing
3. Update step has a new centroid position
4. Assignment step has no change of data points

**Answer:** Option 4: Assignment step has no change of data points

*Explanation:* K-means converges when the assignment step results in no changes - meaning points remain assigned to the same clusters between iterations. This indicates the algorithm has reached a stable state where centroids and cluster assignments no longer change.

---

## Question 3 (1 point)
Which of the following statements about clustering algorithms is true?

**Options:**
1. Clustering algorithms require labeled data for training
2. Clustering algorithms are used to partition data into distinct groups based on similarity
3. Clustering algorithms always produce the same clusters regardless of the initial conditions
4. The k-means clustering algorithm can only be used for datasets with numerical features

**Answer:** Option 2: Clustering algorithms are used to partition data into distinct groups based on similarity

*Explanation:* The fundamental purpose of clustering algorithms is to group similar data points together based on their inherent patterns and similarities, without requiring labeled training data. This makes them unsupervised learning algorithms.

---

# Answer Key
1. Option 3 - Sum of squared distances from points to their centroids (Core metric for measuring cluster cohesion)
2. Option 4 - Assignment step has no change of data points (Convergence criterion)
3. Option 2 - Clustering algorithms partition data into distinct groups based on similarity (Fundamental definition of clustering)