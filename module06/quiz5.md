# DBSCAN and Clustering Quiz

## Question 1 (1 point)
Which clustering algorithm is capable of identifying arbitrarily shaped clusters and is particularly effective in detecting noise?

**Options:**
1. Hierarchical clustering
2. k-means
3. DBSCAN
4. k-means++

**Answer:** Option 3: DBSCAN

DBSCAN (Density-Based Spatial Clustering of Applications with Noise) is uniquely capable of finding arbitrarily shaped clusters based on density. Unlike k-means or hierarchical clustering which assume spherical clusters, DBSCAN can identify clusters of any shape and effectively identify noise points as outliers.

---

## Question 2 (1 point)
In DBSCAN, points that are sufficiently removed from other points are designated as:

**Options:**
1. Border points
2. Core points
3. Cluster centroids
4. Outliers

**Answer:** Option 4: Outliers

In DBSCAN, points that are too far from other points (having fewer than min_samples points within eps radius) are classified as outliers or noise points. These points don't belong to any cluster and represent anomalies in the data.

---

## Question 3 (1 point)
What are the key constructors in the "cluster.DBSCAN()" function in scikit-learn?

**Options:**
1. distance_threshold and min_cluster_size
2. threshold and neighborhood_size
3. min_distance and max_samples
4. eps and min_samples

**Answer:** Option 4: eps and min_samples

The scikit-learn DBSCAN implementation requires two main parameters: eps (the maximum distance between two samples to be considered neighbors) and min_samples (the minimum number of samples in a neighborhood for a point to be considered a core point).

---

## Question 4 (1 point)
How does DBSCAN declare a point as an outlier?

**Options:**
1. A point is considered an outlier if it does not belong to the largest cluster
2. A point is considered an outlier if it lies outside the convex hull of the dataset
3. A point is considered an outlier if it is the farthest point from the dataset's centroid
4. A point is considered an outlier if it has fewer than the minimum number of required neighbors within a specified radius

**Answer:** Option 4: A point is considered an outlier if it has fewer than the minimum number of required neighbors within a specified radius

This is the fundamental definition of an outlier in DBSCAN. Specifically, if a point has fewer than min_samples points within its eps radius neighborhood, it is classified as an outlier/noise point.

---

## Answer Key
1. Option 3 - DBSCAN (Uniquely capable of finding arbitrary-shaped clusters and detecting noise)
2. Option 4 - Outliers (Points with insufficient neighbors are classified as noise)
3. Option 4 - eps and min_samples (Core parameters for DBSCAN implementation)
4. Option 4 - Points with fewer than min_samples neighbors within eps radius (Basic definition of DBSCAN outliers)