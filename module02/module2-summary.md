# Module 2: Fundamentals of Statistics and Distribution Functions

## Key Concepts

### Uniform Distribution
- Simplest distribution type
- Two variants:
  - **Discrete Uniform**: Fixed number of equally probable outcomes between a and b
    - Example: Rolling a die (6 outcomes, probability = 1/n)
    - Variance = (n² - 1)/12
  - **Continuous Uniform**: All values between a and b are equally probable
    - Example: Clock's second hand position (0-360 degrees)
    - Probability density = 1/(b-a)
    - Variance = (b-a)²/12
- Both types have expectation at midpoint between a and b

### Implementation in Python (SciPy)
- Uses `scipy.stats` package
- Uniform distribution parameters:
  - `loc`: Left edge of distribution
  - `scale`: Width of distribution
- Key methods:
  - `pdf()`: Probability density function
  - `rvs()`: Random sampling
  - `mean()`, `var()`, `std()`: Statistical measures

### Normal (Gaussian) Distribution
- Most important distribution in statistics
- Common in natural phenomena (height, temperature, etc.)
- Characterized by:
  - μ (mu): Mean (center of distribution)
  - σ² (sigma squared): Variance
- Bell curve shape
- Ubiquitous due to Central Limit Theorem

### Central Limit Theorem (CLT)
- Key principle: Sample means approach normal distribution as sample size increases
- Applies regardless of original distribution
- Properties:
  1. Sample mean expectation equals population mean
  2. Sample variance decreases as σ²/n
  3. Distribution becomes more normal as n increases
- Practical threshold: n ≥ 30 for normal approximation

### Multivariate Distributions
- Collections of multiple random variables
- Example: Gentoo penguin measurements (beak length, depth)
- Properties:
  - Mean: Vector of individual means
  - Variance: Replaced by covariance matrix
  - Preserves relationships between variables

### Covariance and Correlation
- Covariance Matrix:
  - Diagonal: Individual variances
  - Off-diagonal: Covariances between pairs
  - Symmetric along diagonal
- Correlation:
  - Scaled version of covariance (-1 to 1)
  - Measures linear relationship strength
  - 1: Perfect positive correlation
  - -1: Perfect negative correlation
  - 0: No linear correlation

### Independence vs. Correlation
- Uncorrelated ≠ Independent
- Independence means:
  - Knowing one variable tells nothing about another
  - Conditional distributions are identical to marginal distributions
  - Joint distribution = product of marginal distributions
- Variables can be uncorrelated but dependent (e.g., sine wave relationship)

## Tools and Visualization
- **SciPy.stats**: Primary package for statistical distributions
- **Pandas**: Computing covariance and correlation matrices
- **Seaborn**:
  - Enhanced statistical visualization
  - `pairplot`: Visualize relationships in multivariate data
  - `histplot` with `hue`: Conditional distribution visualization

## Practical Applications
- Quality control in manufacturing
- Natural phenomena measurement
- Economic indicators
- Machine learning model assumptions
- Data analysis and statistical inference