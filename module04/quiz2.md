# DataFrame Operations Quiz

## Question 1 (1 point)
Given two DataFrames (df1 and df2) with two join conditions on columns Entity and Year, what is the statement for joining them into a new DataFrame (df3)?

**Options:**
1. `df3=pd.merge(left=df1, right=df2, left_on="Entity","Year",right_on="Entity","Year")`
2. `df3=pd.merge(left=df1, right=df2, left_on=[Entity,Year],right_on=[Entity,Year]`
3. `df3=pd.merge(left=df1, right=df2, left_on=["Entity","Year"],right_on=["Entity","Year"])`
4. `df3=pd.merge(left=df1, right=df2, left_on=["Entity"],right_on=["Entity])`

**Answer:** Option 3: `df3=pd.merge(left=df1, right=df2, left_on=["Entity","Year"],right_on=["Entity","Year"])`

*Explanation:* The correct syntax for merging DataFrames with multiple conditions requires:
- List of column names in brackets `["column1", "column2"]`
- Matching left_on and right_on parameters
- Properly quoted string column names

---

## Question 2 (1 point)
Consider the following line of code:
```python
df3=pd.merge(left=df1, right=df2, left_on="Entity",right_on="Entity",how=?)
```
What would you give in the "how=" parameter to include all the matching rows from the left table and right tables and "NaN" in the right table for nonmatching rows in the left table?

**Options:**
1. Inner
2. Right
3. Outer
4. Left

**Answer:** Option 4: Left

*Explanation:* A left join (how='left') keeps all records from the left DataFrame and only matching records from the right DataFrame. Non-matching records from the right DataFrame are filled with NaN values.

---

## Question 3 (1 point)
What function is used to drop all null values from a DataFrame?

**Options:**
1. drop_na()
2. dropna()
3. dropnan()
4. drop_null()

**Answer:** Option 2: dropna()

*Explanation:* The pandas method `dropna()` is the correct function to remove rows containing null values from a DataFrame. This is a core pandas function that removes any row containing NaN (Not a Number) or NULL values.

---

## Answer Key
1. Option 3 - `left_on=["Entity","Year"],right_on=["Entity","Year"]` (Proper syntax for multi-column merge)
2. Option 4 - Left (Keeps all left records, fills right non-matches with NaN)
3. Option 2 - dropna() (Standard pandas function for removing null values)