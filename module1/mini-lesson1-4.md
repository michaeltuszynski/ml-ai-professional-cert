# Mini-Lesson 1.4: Analyzing Data Using pandas

As a supplement to Video 1.6: pandas Operations and Plots, this mini-lesson demonstrates how to calculate some common mathematical functions in pandas, such as divide, sum, and percentages. It is common to perform these basic mathematical operations while dealing with data science or ML tasks. Pandas' use of mathematical operations will help with data handling and manipulation.

## Division
To divide two numbers in Python, you can separate the two values using the `/` sign.

```python
df['divide'] = df['column1'] / df['column2']
```

## Summation
To sum two numbers in python, you can add the two values together using the `+` sign.

```python
df['sum'] = df['column1'] + df['column2']
```

## Percentage
While pandas does not natively provide a function to calculate the percentage, this can be done by dividing the column by its sum and then multiplying by 100, as shown below:

```python
df['percent'] = (df['col'] / df['col'].sum()) * 100
```