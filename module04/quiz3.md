# Data Visualization Quiz

## Question 1 (1 point)
Given a DataFrame with the columns Year, Entity, and gdp_ratio, how would you draw a scatterplot to show the trends of GDP ratio per year for each entity?

**Options:**
1. `px.scatter(df, x= "Year", y = "gdp_ratio")`
2. `px.scatter(df, x= Year, y = gdp_ratio , color = "Entity")`
3. `px.scatter(df, x= "Year", y = "gdp_ratio" , color = "Entity")`
4. `px.scatter(df, x= Year, y = gdp_ratio , size = Entity)`

**Answer:** Option 3: `px.scatter(df, x= "Year", y = "gdp_ratio" , color = "Entity")`

*Explanation:* The correct syntax requires string literals for column names ("Year", "gdp_ratio") and uses the `color` parameter to distinguish between entities. This creates a scatterplot where each entity's data points are shown in different colors, making trends easily visible.

---

## Question 2 (1 point)
Given a DataFrame df1 with the columns Entity, Code, Year, and Expectancy, how can it be filtered into a DataFrame without the column Code?

**Options:**
1. `df1=df1[["Entity"."Year"."Expectancy"]]`
2. `df1=df1[["Entity","Year","Expectancy"]]`
3. `df1=df1["Entity","Year","Expectancy"]`
4. `df1=df1[[Entity,Year,Expectancy]]`

**Answer:** Option 2: `df1=df1[["Entity","Year","Expectancy"]]`

*Explanation:* In pandas, to select multiple columns, you use double square brackets with a list of column names as strings. The syntax requires proper string formatting with commas separating the column names.

---

## Question 3 (1 point)
Which attribute of scatter points can be used to visualize additional information?

**Options:**
1. color
2. shape
3. line_dash
4. opacity

**Answer:** Option 1: color

*Explanation:* Color is a fundamental visual attribute in scatter plots that can effectively encode an additional dimension of data. It allows for clear differentiation between categories or continuous values while maintaining readability.

---

# Answer Key
1. Option 3 (`px.scatter` with proper string syntax and color parameter - enables multi-entity visualization)
2. Option 2 (Correct pandas column selection syntax with double brackets and string column names)
3. Option 1 (Color is a primary visual encoding attribute for additional data dimensions)