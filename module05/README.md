# Coupon Acceptance Analysis  Assingment 5.1

## Overview
This project analyzes customer behavior regarding coupon acceptance in various driving scenarios. The goal is to distinguish between customers who accepted a driving coupon versus those who did not.

## Data
The dataset used in this analysis is from the UCI Machine Learning Repository and was collected via a survey on Amazon Mechanical Turk. It includes information about different driving scenarios and whether the driver accepted a coupon.

## Project Structure
- `Practical_Application_1.ipynb`: Jupyter Notebook containing the data analysis for Assignment 5.1
- `data/`: Directory containing the dataset
- `README.md`: This file, providing an overview of the project
- `non_technical_report_assignment5_1.docx`: Word document with a non-technical summary of findings
- `directions.md` : Directions from the portal for reference

## How to Run
1. Clone this repository
2. Ensure you have Jupyter Notebook installed, along with the required libraries (pandas, numpy, matplotlib, seaborn)
3. Open `Practical_Application_1.ipynb` in Jupyter Notebook
4. Run the cells in order to reproduce the analysis

## Key Findings and Recommendations
### Bar Coupon Analysis

1. **Overall Acceptance Rate**:
   - 41% of customers accepted the bar coupons.

2. **Key Factors Influencing Acceptance**:
   - Frequency of bar visits: Those who visit bars more than once a month were more likely to accept coupons.
   - Age: Drivers under 30 had a higher acceptance rate.
   - Occupation: Students showed higher acceptance rates.
   - Passengers: Presence of friends in the car increased likelihood of acceptance.
   - Time of day: Evening coupons were more popular.
   - Marital status: Single individuals were more likely to accept.

3. **Specific Group Insights**:
   - Drivers who visit bars more than once a month and are over 25 had a 69% acceptance rate.
   - Drivers who visit bars more than once a month and don't have kids had a 71% acceptance rate.
   - Acceptance rate was highest (76%) for those who visit bars more than once a month, are under 30, and don't have kids.

### Coffee House Coupon Analysis

1. **Overall Acceptance Rate**:
   - Approximately 50% of customers accepted coffee house coupons.

2. **Key Factors Influencing Acceptance**:
   - Age: Younger individuals (20-30) were more likely to accept coupons.
   - Income: Higher income groups showed lower acceptance rates.
   - Time of Day: Afternoon coupons had higher acceptance rates.
   - Passengers: Presence of friends or partners increased acceptance likelihood.
   - Coffee consumption frequency: Regular coffee drinkers were more receptive.

3. **Statistical Findings**:
   - Chi-square tests confirmed significant relationships between categorical variables (like age groups, income levels) and coupon acceptance.
   - T-tests revealed significant differences in acceptance rates across various demographic groups.

4. **Recommendations**:
   - Target younger demographics and afternoon time slots for higher acceptance rates.
   - Tailor offers based on income levels and social context (presence of passengers).
   - Focus marketing efforts on frequent coffee drinkers for better campaign results.

See `non_technical_report_assignment5_1.docx`