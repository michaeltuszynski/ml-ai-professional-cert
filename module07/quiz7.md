# Quiz 7: Data Processing and Model Predictions

## Question 1 (1 point)
What is one-hot encoding used for?

**Options:**
1. Handling categorical variables in machine learning models
2. Scaling numerical data to improve model performance
3. Encoding ordinal data into numerical values
4. Converting continuous data into discrete categories

**Answer:** Option 1: Handling categorical variables in machine learning models

*Explanation:* One-hot encoding is a technique specifically designed to convert categorical variables into a format that can be provided to machine learning algorithms. It creates binary columns for each category, representing the presence (1) or absence (0) of that category.

---

## Question 2 (1 point)
What is the function in Python that is used for concatenating two dataframes?

**Options:**
1. describe()
2. concat()
3. merge()
4. head()

**Answer:** Option 2: concat()

*Explanation:* pandas.concat() is the primary function used to concatenate (combine) two or more DataFrame objects along either rows or columns.

---

## Question 3 (1 point)
Given a dataframe with coefficients [0.093, 0.187, 0.668, 0.745, 0.621, and 0.732] for features [total_bill, size, Thur, Fri, Sat, Sun]:

```python
   total_bill  size  Thur  Fri  Sat  Sun
0      16.99     2     0    0    0    1
1      10.34     3     0    0    0    1
2      21.01     3     0    0    0    1
3      23.68     2     0    0    0    1
4      24.59     4     0    0    0    1
```

What tip would the model predict for a party of three with a $50 total bill eating on a Thursday?

**Options:**
1. $5.95
2. $5.83
3. $6.88
4. $5.88

**Answer:** Option 4: $5.88

*Explanation:* Using the linear model with given coefficients:
- total_bill contribution: 50 × 0.093 = 4.65
- size contribution: 3 × 0.187 = 0.561
- Thursday contribution: 1 × 0.668 = 0.668
- Other days contribution: 0
Total prediction = $5.88

---

## Answer Key
1. Option 1 - Handling categorical variables (Fundamental data preprocessing technique)
2. Option 2 - concat() (Core pandas function for combining DataFrames)
3. Option 4 - $5.88 (Calculated using linear model coefficients)