# Pandas DataFrame Operations Quiz

## Question 1 (1 point)
With the DataFrame:
```python
df = pd.DataFrame({'A':[0.1,0.2,0.3], 'B':[10,20,30]})
```
What does the statement `df['B'].sum()` return?

**Options:**
1. 20
2. 10
3. 30
4. 60

**Answer:** Option 4: 60

**Explanation:** The `sum()` method adds all values in the specified column. For column 'B', we have 10 + 20 + 30 = 60.

---

## Question 2 (1 point)
With the same DataFrame, what is the correct syntax to add columns A and B?

**Options:**
1. `df['A'].add(df['B'])`
2. `df['A'].add.df['B']`
3. `df[A].add(df[B])`
4. `df['A']add(df['B'])`

**Answer:** Option 1: `df['A'].add(df['B'])`

**Explanation:** In pandas, the `add()` method is used to add two Series objects. The correct syntax requires proper string indexing with quotes and the method call with parentheses.

---

## Question 3 (1 point)
With the DataFrame:
```python
df = pd.DataFrame({'A':[0.1,0.2,0.3], 'B':[10,20,30], 'C':[1,2,3]})
```
How would you create a histogram that includes columns B and C?

**Options:**
1. `df.plot[kind = hist, y =['B','C']`
2. `df.plot(kind = 'hist',y=['B','C'])`
3. `df.plot(kind = 'scatter',y=['B','C'])`
4. `df.plot(kind = 'hist',y=['B','A'])`

**Answer:** Option 2: `df.plot(kind = 'hist',y=['B','C'])`

**Explanation:** To create a histogram in pandas, use the `plot()` method with `kind='hist'` and specify the columns to plot using the `y` parameter as a list.

---

## Question 4 (1 point)
What is the correct code to plot a line chart with columns A and B from a DataFrame df?

**Options:**
1. `df.plot(kind='line',x='index',x=['A','B'])`
2. `df.plot(kind='line',y='index',y=['A','B'])`
3. `df.plot(kind='line',x='A',y =('B')`
4. `df.plot(kind='line',x='index',y=['A','B'])`

**Answer:** Option 4: `df.plot(kind='line',x='index',y=['A','B'])`

**Explanation:** For a line plot, we specify `kind='line'`, use the index for the x-axis, and list the columns to plot on the y-axis in a list format.

---

## Question 5 (1 point)
In the plot() function, what does the parameter figsize=(1,2) specify?

**Options:**
1. The width of the plot
2. The rows of data to plot
3. The width and height of the plot
4. The height of the plot

**Answer:** Option 3: The width and height of the plot

**Explanation:** The `figsize` parameter takes a tuple of two numbers representing the width and height of the figure in inches.

---

# Answer Key
1. Option 4: 60 (Sum of column B: 10+20+30)
2. Option 1: `df['A'].add(df['B'])` (Proper pandas method syntax)
3. Option 2: `df.plot(kind = 'hist',y=['B','C'])` (Histogram plotting syntax)
4. Option 4: `df.plot(kind='line',x='index',y=['A','B'])` (Line plot syntax)
5. Option 3: The width and height of the plot (Figure dimensions in inches)