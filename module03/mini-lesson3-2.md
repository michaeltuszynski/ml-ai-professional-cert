# Mini-Lesson 3.2: pandas, seaborn, and Plotly

Pandas, seaborn, and Plotly are standard Python packages used to build visualizations. Below, you can read about the basics of each library and their respective advantages and disadvantages.

## pandas

[Pandas](https://pandas.pydata.org/) is a powerful data manipulation library built on top of NumPy. It provides data structures such as Series (one-dimensional labeled array) and DataFrame (two-dimensional labeled data structure with columns of potentially different types) that make working with structured data easy and intuitive. Pandas is widely used for data cleaning, transformation, and analysis tasks.

### Common Syntaxes Used in pandas

#### Loading Data
```python
pd.read_csv('file.csv')      # Load data from a CSV file into a DataFrame
pd.read_excel('file.xlsx')   # Load data from an Excel file into a DataFrame
```

#### Viewing Data
```python
df.head()   # View the first few rows of a DataFrame
df.tail()   # View the last few rows of a DataFrame
df.shape    # Get the shape (rows, columns) of the DataFrame
```

#### Indexing and Selection
```python
df['column_name']                    # Select a single column by name
df[['column1', 'column2']]          # Select multiple columns by name
df.loc[row_label, column_label]     # Select a single element by row and column labels
df.iloc[row_index, column_index]    # Select a single element by row and column indices
```

#### Filtering Data
```python
df[df['column'] > value]        # Filter rows based on a condition
df.query('column > value')      # Filter rows using a query string
```

#### Sorting Data
```python
df.sort_values('column')                # Sort DataFrame by values in a single column
df.sort_values(['column1', 'column2'])  # Sort DataFrame by values in multiple columns
```

#### Grouping and Aggregating
```python
df.groupby('column').mean()                         # Group data by a column and calculate the mean
df.groupby('column').agg({'column2': 'sum'})       # Group by one column and aggregate another column
```

#### Creating and Modifying Columns
```python
df['new_column'] = value                           # Create a new column with a constant value
df['new_column'] = df['column1'] + df['column2']   # Create a new column based on existing columns
```

#### Missing Data
```python
df.isnull()      # Check for missing values in the DataFrame
df.dropna()      # Drop rows with missing values
df.fillna(value) # Fill missing values with a specified value
```

#### Merging and Joining DataFrames
```python
pd.concat([df1, df2])                         # Concatenate two DataFrames vertically
pd.merge(df1, df2, on='key_column')           # Merge two DataFrames based on a common column
```

#### Pivot Tables
```python
pd.pivot_table(df,
              values='value_column',
              index='index_column',
              columns='column_to_pivot')       # Create a pivot table
```

## seaborn

[Seaborn](https://seaborn.pydata.org/) is an open-source Python data visualization library built on top of Matplotlib. It provides an intuitive interface for drawing attractive visualizations similar to the ggplot2 library in R. This library offers more robust built-in statistical functions that handle density estimates, confidence bounds, and regression functions.

### Common Syntaxes Used in seaborn

#### Creating Plots
```python
sns.lineplot(x='x_column', y='y_column', data=df)     # Create a line plot
sns.barplot(x='x_column', y='y_column', data=df)      # Create a bar plot
sns.countplot(x='x_column', data=df)                  # Create a count plot
sns.boxplot(x='x_column', y='y_column', data=df)      # Create a box plot
sns.violinplot(x='x_column', y='y_column', data=df)   # Create a violin plot
sns.heatmap(data=df.corr(), annot=True)              # Create a heatmap
```

#### Customizing Plots
```python
sns.set_palette('Set1')           # Set the color palette
plt.title('Title')               # Set the title
plt.xlabel('x_label')           # Set x-axis label
plt.ylabel('y_label')           # Set y-axis label
```

#### Pair Plots
```python
g = sns.PairGrid(df)                            # Create a PairGrid
g.map_diag(sns.histplot)                        # Map diagonal plots
g.map_offdiag(sns.scatterplot)                  # Map off-diagonal plots
```

#### Joint Plots
```python
sns.jointplot(x='x_column', y='y_column', data=df, kind='scatter')
```

#### Regression Plots
```python
sns.regplot(x='x_column', y='y_column', data=df)
sns.lmplot(x='x_column', y='y_column', data=df, hue='hue_column')
```

## Plotly

[Plotly](https://plotly.com/) is a library for creating interactive plots and dashboards. It supports a wide range of plot types and provides interactive features for zooming, panning, and hovering over data points.

### Common Syntax Used in Plotly

#### Creating Basic Plots
```python
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name='line_name'))
fig.update_layout(title='Plot Title',
                 xaxis_title='X Axis Title',
                 yaxis_title='Y Axis Title')
```

#### Different Types of Plots
```python
go.Scatter()     # Scatter Plot
go.Bar()         # Bar Chart
go.Scatter(mode='lines')    # Line Plot
go.Heatmap()     # Heatmap
go.Pie()         # Pie Chart
go.Box()         # Box Plot
```

#### Customizing Plots
```python
fig.update_traces(marker=dict(color='blue'))    # Update marker color
fig.update_layout(showlegend=False)             # Hide legend
fig.update_xaxes(tickangle=45)                  # Rotate x-axis labels
fig.update_yaxes(title_text='Y Axis Title')     # Update y-axis title
```

#### Annotations and Shapes
```python
fig.add_annotation(x=x_value, y=y_value, text='Annotation Text', showarrow=True)
fig.add_shape(type='line', x0=x0_value, y0=y0_value, x1=x1_value, y1=y1_value)
```

#### Subplots
```python
from plotly.subplots import make_subplots
fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Scatter(...), row=1, col=1)
```

#### Exporting Plots
```python
fig.write_html('plot.html')    # Export to HTML
fig.show()                     # Display plot
```

## Comparison of Visualization Libraries

| Library | Pros | Cons |
|---------|------|------|
| pandas | - High-level API<br>- Easier to create plots directly from Python<br>- Nicely integrated with pandas data formats | - Default plots are plain<br>- Plot types are limited<br>- Static charts |
| seaborn | - More desirable chart styling<br>- Statistical graphics capabilities<br>- Matplotlib-based<br>- Can be integrated with other Matplotlib libraries | - Limited chart types<br>- Requires installation<br>- Static charts |
| Plotly | - Interactive and informative plots<br>- Statistical analysis capabilities<br>- Flexible and well-documented<br>- Simple integration with multiple libraries | - No direct method to work offline<br>- Encourages cloud platform |

## Conclusion

While all of these tools excel at data visualization, each has its trade-offs. Pandas and seaborn provide static charts but offer different advantages in terms of integration and statistical capabilities. Plotly stands out for interactive visualizations but may require additional consideration for offline use. The choice of library will ultimately depend on your specific needs and use case.