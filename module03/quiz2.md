# Data Visualization in Python Quiz

## Question 1 (1 point)
Which statement do you need to use in Python for the DataFrame df to build a bar plot between the columns Entity and GDP?

Given DataFrame:
```python
Entity	Code	Year	GDP (constant 2010 US$)	gdp
8494	United States	USA	2017	1.730498e+13	17304.984279
1783	China	CHN	2017	1.016101e+13	10161.012759
4261	Japan	JPN	2017	6.158329e+12	6156.328721
3130	Germany	DEU	2017	3.865759e+12	3865.759081
8436	United Kingdom	GBR	2017	2.806903e+12	2806.903097
3789	India	IND	2017	2.629542e+12	2629.542212
```

**Options:**
1. `df.plot(x="Entity",y="gdp")`
2. `df.plot(x="Entity",kind="bar")`
3. `df.plot(x="Entity",y="gdp",kind="bar")`
4. `df.plot(x="Entity",y="gdp",kind="plot")`

**Answer:** Option 3: `df.plot(x="Entity",y="gdp",kind="bar")`
- Core definition: To create a bar plot in pandas, you need to specify both x and y columns along with kind="bar"
- The x parameter defines the categories (Entity), y specifies the values to plot (gdp), and kind="bar" sets the plot type

## Question 2 (1 point)
What is the function that rotates the x-axis labels of a plot built with Seaborn?

**Options:**
1. `xticks.rotation`
2. `xticks(rotation)`
3. `yticks(rotation)`
4. `xticks"rotation"`

**Answer:** Option 2: `xticks(rotation)`
- Core definition: In matplotlib/seaborn, axis label rotation is controlled through the xticks() function with a rotation parameter
- This is a common customization for improving readability when x-axis labels are long or overlapping

## Question 3 (1 point)
Which of the following is the function to plot a bar chart using Plotly?

**Options:**
1. `sns.barplot(df,x="Entity",y="gdp")`
2. `df.plot(x="Entity",y="gdp",kind="bar")`
3. `fig=px.bar(df,x="Entity",y="gdp",color="Entity")`
4. `plt.bar("Entity",'gdp")`

**Answer:** Option 3: `fig=px.bar(df,x="Entity",y="gdp",color="Entity")`
- Core definition: Plotly Express uses px.bar() as its primary bar chart function
- The color parameter is a unique Plotly feature that automatically handles color encoding by category

## Question 4 (1 point)
Which function alters font size in a plot built with Plotly?

**Options:**
1. `fig.update_size(font_size=<VALUE>)`
2. `fig.update_layout(font_size=<VALUE>)`
3. `fig.layout(font_size=<VALUE>)`
4. `fig.update(font_size=<VALUE>)`

**Answer:** Option 2: `fig.update_layout(font_size=<VALUE>)`
- Core definition: Plotly uses update_layout() as the main method for modifying figure properties
- This function allows global styling changes including font sizes across the entire figure

---

# Answer Key
1. Option 3: `df.plot(x="Entity",y="gdp",kind="bar")` (Requires x, y, and kind parameters for proper bar plot)
2. Option 2: `xticks(rotation)` (Standard matplotlib/seaborn function for rotating x-axis labels)
3. Option 3: `fig=px.bar(df,x="Entity",y="gdp",color="Entity")` (Plotly Express syntax for bar charts)
4. Option 2: `fig.update_layout(font_size=<VALUE>)` (Plotly's method for updating figure properties)