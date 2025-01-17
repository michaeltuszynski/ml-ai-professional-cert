# Module 6: Data Clustering and Principal Component Analysis (PCA) - Video Summary

## Video 1: Singular Value Decomposition (SVD)

### Main Topic and Key Concepts
- Introduction to unsupervised learning algorithms: k-means clustering and PCA
- Focus on pattern finding in data without using output/training data
- Dataset assumptions: real numbers only, N rows (samples), D columns (features)

### Pattern Finding Approaches
- PCA: Finds patterns in columns through linear combinations
- k-means: Finds patterns in rows by creating groups
- Key difference: Not simply transposes of each other

### Technical Example
- Temperature measurements from 100 cities using two thermometers (Fahrenheit and Centigrade)
- High correlation (0.99) between measurements
- Linear relationship: 1.8C – F + 32 = 0
- Goal: Reduce dimensionality for model training

### Best Practices
- Avoid using highly correlated inputs
- Consider curse of dimensionality
- Maximize variance in input data
- Project data onto optimal directions

## Video 2: Principal Component Analysis (PCA)

### Implementation Steps
1. Normalize data
   - Shift data cloud to origin
   - Normalize for unit standard deviation
2. Perform SVD on normalized data
3. Verify decomposition correctness

### Technical Details
- Uses SciPy's SVD implementation
- Matrix factorization: X = U @ Sigma @ V.T
- Verification using numpy.allclose()
- Recovery of original data through denormalization

### Code Components
```python
# Normalization
mu = X.mean()
sigma = X.std()
Xnorm = (X - mu)/sigma

# SVD Decomposition
U, s, Vt = svd(Xnorm, full_matrices=False)
Sigma = np.diag(s)
V = Vt.T

# Verification
assert np.allclose(Xnorm, U @ Sigma @ V.T)
```

## Video 3: Interpretation of Principal Component Analysis (PCA)

### Key Components
- U, Sigma, and V matrices interpretation
- Principal components as rank-1 matrices
- Singular values significance
- Approximation sequence construction

### Technical Aspects
- V columns as optimal projection directions
- Singular values ordered largest to smallest
- Cumulative variance calculation
- Dimensionality reduction decisions

### Best Practices
- Use cumulative singular values plot for dimension selection
- Consider variance preservation threshold (e.g., 90%)
- Balance dimensionality reduction with information preservation

## Video 4: PCA (Continued)

### Implementation Details
- Projection to lower dimensional space
- Handling new data points
- Matrix operations for projections

### Code Example
```python
# Projection to r dimensions
r = 4  # number of dimensions to keep
Ur = U[:,:r]
Sigmar = Sigma[:r,:r]
Xrr = pd.DataFrame(Ur @ Sigmar)

# Projecting new data
newhome_norm = (newhome - mu)/sigma
newhome_proj = newhome_norm @ V[:,:r]
```

## Video 5: SVD and PCA Summary

### Key Points
- Two-step PCA process: centering data and SVD
- V matrix contains projection directions
- Singular values indicate component significance
- New data handling through centering and projection

### Best Practices
- Use cumulative singular values for dimension selection
- Consider scikit-learn's implementation for simplified workflow
- Properly handle new data points

## Video 6: Clustering and k-means

### Main Concepts
- Clustering as unsupervised learning
- k-means algorithm mechanics
- Centroid-based clustering approach

### Algorithm Steps
1. Initial centroid placement
2. Point assignment to nearest centroid
3. Centroid position update
4. Repeat until convergence

### Best Practices
- Run multiple initializations
- Select optimal K using elbow method
- Consider inertia plots for cluster number selection

### Technical Considerations
- Inertia as optimization metric
- Impact of initial centroid placement
- Convergence guarantees

## Video 7: Clustering in Scikit-learn

### Implementation Details
```python
# Basic k-means
kmeans = cluster.KMeans(n_clusters=5, init='random')
kmeans.fit(X)

# k-means++
kmeanspp = cluster.KMeans(n_clusters=5, init='k-means++', verbose=1)
kmeanspp.fit(X)

# DBSCAN
dbscan = DBSCAN(eps=9, min_samples=3).fit(X)
```

### Key Features
- k-means++ initialization strategy
- Verbose output for algorithm progress
- DBSCAN as alternative clustering method

### Case Study
- Mall shoppers dataset analysis
- Customer segmentation based on income and spending
- Prediction capabilities for new customers

## Video 8: DBSCAN

### Key Features
- Centroidless algorithm
- Natural cluster number determination
- Curved boundary capability
- Built-in outlier detection

### Technical Parameters
- epsilon (radius)
- min_samples (minimum points)
- Core points, boundary points, and outliers

### Advantages over k-means
- No random initialization needed
- Single run sufficiency
- Non-linear cluster boundary capability
- Natural outlier detection

### Best Practices
- Consider parameter sensitivity
- Understand trade-offs between algorithms
- Choose based on specific problem requirements

### Tools and Libraries Mentioned
- NumPy
- pandas
- scikit-learn
- SciPy
- Matplotlib