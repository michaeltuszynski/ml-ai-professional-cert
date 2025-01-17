# Python DataFrame Operations Quiz

## Question 1 (1 point)
In Python, what is the correct syntax for loading a DataFrame from a csv file?

**Options:**
1. `df=read_csv(filename)`
2. `df=pd.read_csv'filename'`
3. `df=pd.readcsv(filename)`
4. `df=pd.read_csv(filename)`

**Answer:** Option 4: `df=pd.read_csv(filename)`

*Explanation:* The correct syntax requires:
- Using the pandas library (referenced by `pd`)
- The method `read_csv()` with parentheses
- A filename parameter inside the parentheses

---

## Question 2 (1 point)
In Python, what will `df.sample(10)` return?

**Options:**
1. Ten random rows of the DataFrame df
2. The middle ten rows of the DataFrame df
3. The top ten rows of the DataFrame df
4. The last ten rows of the DataFrame df

**Answer:** Option 1: Ten random rows of the DataFrame df

*Explanation:* The `sample()` method in pandas:
- Randomly selects rows from the DataFrame
- Returns the specified number of rows (10 in this case)
- Sampling is done without replacement by default

---

## Question 3 (1 point)
For the DataFrame shown in Video 3.2, you want to show only the rows of data from China. Which would be the correct syntax?

Example DataFrame:
```
Entity	Code	Year	GDP (constant 2010 US$)
6856	Saint Lucia	LCA	2009	1.404756e+09
1479	Canada	CAN	1983	8.031318e+11
6277	Papua New Guinea	PNG	1962	2.579601e+09
6073	Oman	OMN	1974	7.085347e+09
8279	Uganda	UGA	1992	5.751489e+09
```

**Options:**
1. `df[df["Entity"]=="China"]`
2. `df[df[Entity]=="China"]`
3. `df["Entity"]=="China"`
4. `df[df["Entity"]==China]`

**Answer:** Option 1: `df[df["Entity"]=="China"]`

*Explanation:* The correct syntax requires:
- Double square brackets for boolean indexing
- Column name "Entity" in quotes
- Comparison value "China" in quotes
- Proper boolean indexing structure

---

## Question 4 (1 point)
In Python, given the list `list_of_countries=["UK","USA","China","Egypt"]`, which of the following statements accurately describes the purpose of `df.query('Entity in @list_of_countries')`?

**Options:**
1. It selects rows from the DataFrame df where the "Entity" column does not match any value in list_of_countries
2. It selects rows from the DataFrame df where the "Entity" column partially matches any value in list_of_countries
3. It selects rows from the DataFrame df where the "Entity" column matches all values in list_of_countries
4. It selects rows from the DataFrame df where the "Entity" column matches any value in list_of_countries

**Answer:** Option 4: It selects rows from the DataFrame df where the "Entity" column matches any value in list_of_countries

*Explanation:* The `query()` method with `in @variable_name`:
- Uses the `@` symbol to reference Python variables
- Checks if values in the "Entity" column exist in the list
- Returns rows where there's a match with any value in the list

---

## Answer Key
1. Option 4 (Using pandas read_csv with proper syntax)
2. Option 1 (Random sampling of DataFrame rows)
3. Option 1 (Correct boolean indexing syntax for DataFrame filtering)
4. Option 4 (DataFrame query method with list membership)