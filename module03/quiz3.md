# Data Analysis Quiz 3

## Question 1 (1 point)
For a DataFrame df, given a column name "gdp," what would be the statement in Python to sort the DataFrame by GDP?

**Options:**
1. `df.sort.values("Column")`
2. `df.sort_values("gdp")`
3. `df.sort_values(gdp)`
4. `df.sort("gdp")`

**Answer:** Option 2: `df.sort_values("gdp")`
- Core definition: The `sort_values()` method is pandas' primary function for sorting DataFrames
- Implementation detail: It takes a column name as a string parameter
- The method properly handles both ascending and descending sorts

---

## Question 2 (1 point)
Suppose you have the Python statement `df.groupby("column").agg(sum)`. Instead of using `.agg(sum)`, what would be the built-in function to aggregate on a summation?

**Options:**
1. `.summation()`
2. `.sum()`
3. `.summ()`
4. `.agg(s)`

**Answer:** Option 2: `.sum()`
- Core definition: `.sum()` is pandas' built-in method for calculating column sums
- Implementation detail: It's a direct shorthand for `.agg(sum)`
- More efficient and cleaner syntax than using the aggregation function

---

## Question 3 (1 point)
Given the following table of furniture exports:

```
Entity  Year  Value
China   1960  1.00
India   1960  1.00
USA     1960  1.00
China   1990  6.48
India   1990  3.41
USA     1990  2.94
China   2017  79.40
India   2017  19.20
USA     2017  5.62
```

Using the code:
```python
result = df.groupby('Entity').agg({'Column': 'sum'}).max()
entity_with_max_sum = result['Column'].idxmax()
```

Which country has the maximum .agg(sum), and what is the value?

**Options:**
1. USA; 79.4
2. USA; 9.56
3. India; 23.61
4. China; 86.88

**Answer:** Option 4: China; 86.88
- Core calculation: Sum of China's values (1.00 + 6.48 + 79.40 = 86.88)
- Implementation detail: The groupby operation aggregates all values for each country
- China has the highest total across all years

---

# Answer Key
1. Option 2: `df.sort_values("gdp")` (Standard pandas method for sorting DataFrames)
2. Option 2: `.sum()` (Built-in pandas aggregation method)
3. Option 4: China; 86.88 (Highest sum of values across all years)