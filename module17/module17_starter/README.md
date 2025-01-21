# Bank Marketing Campaign Analysis

## Overview
This project analyzes a Portuguese banking institution's marketing campaigns to predict term deposit subscriptions, aiming to improve campaign efficiency and reduce customer contact costs. The analysis compares multiple machine learning classifiers to determine the most effective prediction approach.

## Business Understanding
The bank needs to optimize their telephone marketing campaigns by identifying customers most likely to subscribe to term deposits. This helps:
- Reduce operational costs
- Increase campaign success rate
- Improve customer targeting
- Optimize resource allocation

## Data Description
Dataset from UCI Machine Learning Repository contains:
- 41,188 contacts from May 2008 to November 2010
- Client demographics (age, job, marital status, education)
- Campaign information (contact type, duration, previous attempts)
- Economic context indicators
- Target: term deposit subscription (yes/no)

## Key Findings
1. Model Performance:
   - Logistic Regression: 94.4% (best performer)
   - Decision Tree: 94.1%
   - K-Nearest Neighbors: 88.6%

2. Important Predictors:
   - Economic indicators strongly influence subscription likelihood
   - Previous campaign success is a key indicator
   - Contact duration correlates with success

3. Actionable Insights:
   - Focus on customers with previous successful interactions
   - Time marketing campaigns with favorable economic indicators
   - Optimize call duration based on customer profile

## Recommendations
1. Implement automated scoring system using logistic regression
2. Prioritize customer segments with highest predicted success rates
3. Adjust campaign timing based on economic indicators
4. Develop targeted scripts for different customer profiles

## Technologies Used
- Python (pandas, scikit-learn)
- Jupyter Notebooks
- Machine Learning: Logistic Regression, Decision Trees, KNN
- Cross-validation and Grid Search for optimization

## Repository Structure
- `prompt_III.ipynb`: Main analysis notebook
- `data/`: Contains the bank marketing dataset
- `README.md`: Project documentation

## Future Improvements
1. Feature engineering opportunities
2. Ensemble methods exploration
3. Cost-sensitive learning implementation
4. Real-time prediction system development