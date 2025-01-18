# Module 7 Office Hours Session 2 - Car Price Prediction using Linear Regression

## Overview
- Focus on practical application of linear regression for car price prediction
- Using a dataset with 11,000 entries and 15 columns of car-related features
- Goal: Predict MSRP (Manufacturer's Suggested Retail Price) based on car features

## Linear Regression Fundamentals Review
- Explained as weighted average of different coefficients
- Example using sales prediction based on price and advertisement
- Formula: Y = β₁X₁ + β₂X₂ (where β are coefficients)

## Dataset Features
### Input Variables
- Make (manufacturer)
- Model
- Engine fuel type
- Engine horsepower
- Engine cylinders
- Transmission
- Driven wheels
- Vehicle type
- Market category
- Vehicle size
- Vehicle style
- Highway MPG
- City MPG

### Target Variable
- MSRP (price to predict)

## Data Preprocessing Steps
1. Handling Categorical Data
   - Using one-hot encoding for categorical variables
   - Converting text data into numerical format

2. Data Analysis
   - Examining MSRP distribution
   - Creating correlation matrices
   - Analyzing relationships between features
   - Identifying key predictors (e.g., engine horsepower showing strong correlation)

3. Feature Engineering
   - Log transformation of MSRP for better distribution
   - Z-score calculation for normalization
   - Handling outliers in the data

## Model Development
- Focus on numerical features initially:
  - Engine horsepower
  - Engine cylinders
  - Number of doors
  - Highway MPG
  - City MPG

## Best Practices Covered
- Using sample() instead of head() for better data overview
- Importance of data visualization
- Handling categorical variables
- Feature selection based on correlation
- Data transformation techniques

## Additional Notes
- Discussion of practical applications (used car pricing, house pricing)
- Emphasis on understanding feature relationships
- Importance of data preprocessing in model performance

## Recommendations
- Try different variations of the model with:
  - Log-transformed MSRP
  - Different feature combinations
  - Various preprocessing techniques

## Interactive Elements
- Hands-on coding demonstration
- Q&A sessions with participants
- Real-world application discussions