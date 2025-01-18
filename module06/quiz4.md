# Quiz 4: Data Analysis and K-means Clustering

## Question 1 (1 point)
Consider this dataframe:

| CustomerID | Gender | Age | Annual Income (k$) | Spending Score (1-100) |
|-----------|--------|-----|-------------------|----------------------|
| 1         | Male   | 19  | 15               | 39                   |
| 2         | Male   | 21  | 15               | 81                   |
| 3         | Female | 20  | 16               | 6                    |
| 4         | Female | 23  | 16               | 77                   |
| 5         | Female | 31  | 17               | 40                   |
| ...       | ...    | ... | ...              | ...                  |
| 196       | Female | 35  | 120              | 79                   |
| 197       | Female | 45  | 126              | 28                   |
| 198       | Male   | 32  | 126              | 74                   |
| 199       | Male   | 32  | 137              | 18                   |
| 200       | Male   | 30  | 137              | 83                   |

What should the index of this dataframe be set to?

**Options:**
1. Age
2. CustomerID
3. Spending Score (1-100)
4. Gender

**Answer:** Option 2: CustomerID
- CustomerID is the ideal choice for an index as it is unique, non-null, and serves as a natural identifier for each record in the dataset.

## Question 2 (1 point)
In the Python function k-means() from the scikit-learn library, what is the purpose of the init parameter?

**Options:**
1. To determine the number of clusters to form
2. To specify the maximum number of iterations for the k-means algorithm
3. To decide the stopping criterion for convergence
4. To select the criteria for the initialization of centroids

**Answer:** Option 4: To select the criteria for the initialization of centroids
- The init parameter determines how the initial cluster centers are chosen, typically using methods like 'k-means++' or 'random'.

## Question 3 (1 point)
In "k-means()," how do you generate the array that tells which cluster the data point belongs to?

**Options:**
1. k-means(labels)
2. k-means(labels_)
3. k-means.labels_
4. k-means.labels

**Answer:** Option 3: k-means.labels_
- The labels_ attribute (with underscore) is the correct property to access cluster assignments after fitting the model.

---

## Answer Key
1. Option 2: CustomerID (Unique identifier for each record)
2. Option 4: To select the criteria for the initialization of centroids (Controls how initial cluster centers are chosen)
3. Option 3: k-means.labels_ (Correct attribute to access cluster assignments)