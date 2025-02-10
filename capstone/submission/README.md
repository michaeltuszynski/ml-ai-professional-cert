### Falls Risk Prediction in Older Adults

**Author**: Michael Tuszynski

#### Executive summary
This project analyzes falls risk factors among older adults using the NHATS dataset. Through exploratory data analysis and machine learning, we aim to identify key predictors of falls and develop a baseline model for falls risk prediction.

#### Rationale
Falls among older adults are a significant public health concern, leading to serious injuries, reduced quality of life, and substantial healthcare costs. Early identification of falls risk could enable targeted interventions and prevention strategies.

#### Research Question
Can we predict falls risk in older adults using mobility, health, and demographic factors from the NHATS dataset? What are the key predictors of falls risk?

#### Data Sources
National Health and Aging Trends Study (NHATS) Round 13 dataset, focusing on variables related to:
- Falls history
- Mobility aid usage
- Physical function
- Balance and walking ability
- Pain indicators
- Worry about falls

The data is available from the [NHATS website](https://nhats.org/researcher/data-access/public-use-files) and requires free registration to access the public use files.

#### Methodology
1. Exploratory Data Analysis:
   - Analyzed distributions of falls and related variables
   - Examined relationships between mobility aids and falls
   - Visualized key risk factors

2. Data Preparation:
   - Handled missing values through median imputation
   - Engineered features for mobility aid usage
   - Cleaned special codes in variables

3. Baseline Modeling:
   - Implemented logistic regression with class balancing
   - Evaluated using ROC AUC, sensitivity, and specificity
   - Analyzed feature importance

#### Results
1. Falls Distribution:
   - 11.8% of participants reported falls
   - 88.2% reported no falls

2. Model Performance:
   - ROC AUC Score: 0.696
   - Sensitivity: 0.624 (62.4% of falls correctly identified)
   - Specificity: 0.674 (67.4% of non-falls correctly identified)

3. Key Findings:
   - Mobility aid usage is a significant predictor
   - Worry about falls shows strong association with actual falls
   - Balance and walking indicators contribute to falls risk

#### Next steps
1. Feature Engineering:
   - Create interaction terms between mobility and balance features
   - Incorporate additional health indicators

2. Model Improvements:
   - Implement more sophisticated models (Random Forests, XGBoost)
   - Explore feature selection techniques
   - Consider ensemble methods

3. Additional Analysis:
   - Investigate temporal patterns in falls
   - Analyze demographic subgroups
   - Study impact of interventions

#### Outline of project

- [Falls Prediction EDA Notebook](falls_prediction_eda.ipynb)

##### Contact and Further Information
Mike Tuszynski (miketuszynski42@gmail.com)