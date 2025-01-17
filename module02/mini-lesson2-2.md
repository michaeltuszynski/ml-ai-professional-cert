# Mini-Lesson 2.2: Multivariate Distributions

## Introduction to Multivariate Random Variables

A multivariate random variable consists of two or more random variables, representing a collection of random outcomes. Each outcome corresponds to one of the component random variables.

**Example**: Consider a dataset containing heights and weights of individuals:
- Height and weight are two separate random variables
- Together they form a multivariate random variable (height-weight pair)
- Can be represented as a vector where each element is a component random variable

**Applications**:
- Statistics
- Econometrics
- Machine Learning
- Analysis of relationships between multiple variables

## Covariance

Covariance measures how two random variables change together. For random variables X and Y:

### Mathematical Definition

```
Cov(X,Y) = E[(X - μX)(Y - μY)]
```

Where:
- E is the expected value (mean)
- μX and μY are the means of X and Y respectively

### Practical Formula

```
Cov(X,Y) = (1/n) ∑(xi - x̄)(yi - ȳ)
```

Where:
- n is the number of observations
- xi and yi are individual observations
- x̄ and ȳ are means of X and Y

### Interpretation

- **Positive covariance**: As one variable increases, the other tends to increase
- **Negative covariance**: As one variable increases, the other tends to decrease
- **Zero covariance**: No linear relationship between variables

## Correlation

Correlation measures the strength and direction of the linear relationship between variables.

### Correlation Coefficient (ρ)

```
ρ = Cov(X,Y) / (σx * σy)
```

Where:
- Cov(X,Y) is the covariance between X and Y
- σx and σy are the standard deviations of X and Y respectively

### Properties

1. Always ranges between -1 and +1
2. +1 indicates perfect positive correlation
3. -1 indicates perfect negative correlation
4. 0 indicates no linear correlation