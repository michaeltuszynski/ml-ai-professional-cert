# Module 3 Quiz 4: Pandas DataFrame Operations

---

## Question 1 (1 point)
Which of the following methods is used to set a new index for a DataFrame in pandas?

**Options:**
1. `reset_index()`
2. `reindex()`
3. `setindex()`
4. `set_index()`

**Answer:** Option 4: `set_index()`

*Explanation:* `set_index()` is the primary pandas method for setting a new index in a DataFrame. It allows you to set one or more columns as the index of the DataFrame.

---

## Question 2 (1 point)
Suppose you have a DataFrame df1 that has the columns "Year" and "GDP," with the index set as "Year." You also have a DataFrame df2 that has columns labeled "Year," "Entity," and "GDP."

To get the fraction of the GDP that each entity generates per year, what should be the index of df2?

**Options:**
1. `set_index("Year")`
2. `set_index("Entity","Year")`
3. `set_index("Entity")`
4. `set_index(["Entity","Year"])`

**Answer:** Option 4: `set_index(["Entity","Year"])`

*Explanation:* When creating a hierarchical index for time series data by entity, we need both Entity and Year as index levels. The correct syntax uses a list to specify multiple index columns.

---

## Question 3 (1 point)
What occurs when `groupby("Entity")` and `filter` are used together?

**Options:**
1. Initially, filter filters the output, followed by groupby grouping it into subgroups
2. filter first removes elements not meeting the condition, then groupby groups the remaining elements into subgroups
3. groupby divides "Entity" into subgroups, and filter retains the elements meeting the specified condition
4. groupby divides entities into subgroups, and filter retains all elements, regardless of the condition

**Answer:** Option 3: groupby divides "Entity" into subgroups, and filter retains the elements meeting the specified condition

*Explanation:* In pandas, when using groupby with filter, the groupby operation first creates groups, then the filter is applied to each group based on the specified condition. Only groups that meet the filter condition are retained in the result.

---

## Question 4 (1 point)
Given the DataFrame and the Python statement `df.groupby("Entity").filter(max_gdp_ratio_gt_10)`, which of the following entities of the data will be in the output?

```python
def max_gdp_ratio_gt_10(s):
    max_gdp_ratio = max(s["gdp_ratio"])
    return max_gdp_ratio < 10

# DataFrame
# China     1960    1
# India     1960    1
# USA       1960    1
# China     1990    6.48
# India     1990    3.41
# USA       1990    2.94
# China     2017    79.4
# India     2017    19.2
# USA       2017    5.62
```

**Options:**
1. China
2. India
3. USA

**Answer:** Option 3: USA

*Explanation:* The filter function keeps groups where the maximum GDP ratio is less than 10. Looking at the data:
- China's max is 79.4 (> 10)
- India's max is 19.2 (> 10)
- USA's max is 5.62 (< 10)
Therefore, only USA meets the condition.

---

## Answer Key
1. Option 4: `set_index()` (Primary method for setting DataFrame index)
2. Option 4: `set_index(["Entity","Year"])` (Correct syntax for hierarchical index)
3. Option 3: groupby then filter on groups (Correct order of operations)
4. Option 3: USA (Only entity with max GDP ratio < 10)