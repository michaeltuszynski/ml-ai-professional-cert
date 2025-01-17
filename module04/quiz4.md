# Data Visualization Quiz 4

## Question 1 (1 point)
In which library is `px.histogram(df["column"])` used to create a histogram?

**Options:**
1. pandas
2. Seaborn
3. Bokeh
4. Plotly

**Answer:** Option 4: Plotly
- Core definition: `px` is the Plotly Express module, a high-level interface for Plotly
- The `px.histogram()` function is specifically part of the Plotly Express library for creating interactive histograms

## Question 2 (1 point)
What is the significance of `kde=True` in `sns.displot()`?

**Options:**
1. It creates a scatterplot of the data points, showing the relationship between two variables.
2. It adds a kernel density estimate (KDE) plot to the histogram, showing the estimated probability density function of the data.
3. It changes the style of the plot to a kernel density estimate (KDE) plot, removing the histogram.
4. It adds error bars to the plot, showing the uncertainty in the data.

**Answer:** Option 2: It adds a kernel density estimate (KDE) plot to the histogram, showing the estimated probability density function of the data.
- Core definition: KDE is a non-parametric way to estimate the probability density function of a random variable
- Implementation detail: In Seaborn, `kde=True` overlays this estimate on top of the histogram

## Question 3 (1 point)
What does the middle line of a box plot represent?

**Options:**
1. Mode
2. Median
3. Mean
4. Range

**Answer:** Option 2: Median
- Core definition: The middle line in a box plot represents the median (50th percentile) of the data
- This divides the data into two equal halves, with 50% of the data above and 50% below

## Question 4 (1 point)
In Seaborn, which plot function is used to quickly visualize and analyze the relationship between two variables and describe their individual distributions on the same plot?

**Options:**
1. sns.violinplot()
2. sns.displot()
3. sns.jointplot()
4. sns.boxplot()

**Answer:** Option 3: sns.jointplot()
- Core definition: `jointplot()` creates a multi-panel figure showing both the bivariate relationship between variables and their univariate distributions
- Implementation detail: It combines a scatter plot with histogram/KDE plots on the margins

---

# Answer Key
1. Option 4 - Plotly (The `px` prefix indicates Plotly Express)
2. Option 2 - Adds KDE to histogram (Shows probability density function overlay)
3. Option 2 - Median (Central line showing 50th percentile)
4. Option 3 - sns.jointplot() (Combines bivariate and univariate visualizations)