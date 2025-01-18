# Mini-Lesson 6.3: k-means

k-means clustering is a popular unsupervised ML algorithm used for partitioning a dataset into *k* distinct, non-overlapping clusters. Each data point belongs to the cluster with the nearest mean, serving as a prototype of the cluster. The algorithm iteratively optimizes the placement of the centroids (means) of the clusters until the assignments of data points to clusters no longer change.

## Steps of k-means Clustering

1. **Initialize centroids**: Select *k* initial centroids randomly.
2. **Assign points to nearest centroid**: Assign each data point to the nearest centroid.
3. **Update centroids**: Compute the new centroids as the mean of all points assigned to each centroid.
4. **Repeat**: Repeat steps 2 and 3 until the centroids no longer change or a maximum number of iterations is reached.

## Solved Numerical on k-means Clustering

Consider the following set of points:

Points: (2,10), (2,5), (8,4), (5,8), (7,5), (6,4), (1,2), (4,9)

### Step 1: Initialize Centroids
Randomly pick two initial centroids. For simplicity, choose the first two points as centroids:

Initial centroids: (2,10), (2,5)

### Step 2: Assign Points to Nearest Centroid
We calculate the Euclidean distance from each point to the centroids and assign each point to the nearest centroid.

**Distance from (2,10):**
- (2,10) to (2,10): 0
- (2,5): 5
- (8,4): 10
- (5,8): 5.83
- (7,5): 7.81
- (6,4): 8
- (1,2): 8.06
- (4,9): 2.24

**Distance from (2,5):**
- (2,10): 5
- (2,5): 0
- (8,4): 6.32
- (5,8): 3.61
- (7,5): 5
- (6,4): 4.47
- (1,2): 3.16
- (4,9): 5

**Assign points to the nearest centroid:**

Cluster 1 (centroid (2,10)): (2,10), (5,8), (4,9)
Cluster 2 (centroid (2,5)): (2,5), (8,4), (7,5), (6,4), (1,2)

### Step 3: Update Centroids
Calculate the new centroids as the mean of the points in each cluster:

**New centroid for Cluster 1:**
Mean of (2,10), (5,8), (4,9):
- x = (2+5+4)/3 = 11/3 = 3.67
- y = (10+8+9)/3 = 27/3 = 9
- New centroid = (3.67,9)

**New centroid for Cluster 2:**
Mean of (2,5), (8,4), (7,5), (6,4), (1,2):
- x = (2+8+7+6+1)/5 = 24/5 = 4.8
- y = (5+4+5+4+2)/5 = 20/5 = 4
- New centroid = (4.8,4)

### Step 4: Repeat
Assign points to the new centroids and update centroids until convergence.

**Second iteration:**

*Distance from (3.67,9):*
- (2,10): 2.06
- (2,5): 4.27
- (8,4): 6.86
- (5,8): 1.67
- (7,5): 5.31
- (6,4): 5.83
- (1,2): 7.49
- (4,9): 0.33

*Distance from (4.8,4):*
- (2,10): 6.47
- (2,5): 3.05
- (8,4): 3.2
- (5,8): 4.03
- (7,5): 2.28
- (1,2): 4.31
- (4,9): 5.04

**Final Clusters:**

Cluster 1 (centroid (3.67,9)): (2,10), (5,8), (4,9)
Cluster 2 (centroid (4.8,4)): (2,5), (8,4), (7,5), (6,4), (1,2)

The centroids have not changed, so the algorithm has converged.