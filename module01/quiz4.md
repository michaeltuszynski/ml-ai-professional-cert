# Pandas DataFrame Operations Quiz

## Question 1 (1 point)
What code would you use to create a DataFrame from a variable type dictionary stored as data?

**Options:**
1. `DF=pd.DataFrame'data'`
2. `DF=pd.DataFrame(data)`
3. `DF=pd.DataFrame.data`
4. `DF=pd.DataFrame"data"`

**Answer:** Option 2: `DF=pd.DataFrame(data)`

**Explanation:** The `pd.DataFrame()` constructor takes a dictionary as an argument to create a DataFrame. The parentheses are required for proper function syntax, and the dictionary variable is passed directly without quotes.

## Question 2 (1 point)
What syntax is used to import a .csv file into a DataFrame?

**Options:**
1. `df=read_csv(filename)`
2. `df=pd.readcsv(filename)`
3. `df=pd.read_csv'filename'`
4. `df=pd.read_csv(filename)`

**Answer:** Option 4: `df=pd.read_csv(filename)`

**Explanation:** The correct method in pandas is `pd.read_csv()` which requires the filename as an argument in parentheses. The `pd` prefix is necessary as it's the conventional alias for pandas, and underscores are used in the method name.

## Question 3 (1 point)
Which function is used to get the datatypes of the columns in the DataFrame?

**Options:**
1. `head()`
2. `describe()`
3. `info()`
4. `tail()`

**Answer:** Option 3: `info()`

**Explanation:** The `info()` method provides a concise summary of a DataFrame, including the column datatypes, non-null values count, and memory usage. This is distinct from other methods like `describe()` which shows statistical summaries.

## Question 4 (1 point)
Which of the following functions would show you methods of descriptive statistics?

**Options:**
1. `tail()`
2. `head()`
3. `info()`
4. `describe()`

**Answer:** Option 4: `describe()`

**Explanation:** The `describe()` method generates descriptive statistics including count, mean, std, min, 25%, 50%, 75%, and max for numerical columns in a DataFrame. It provides a statistical summary rather than just displaying data like `head()` or `tail()`.

## Question 5 (1 point)
What will df.head(10) return?

**Options:**
1. Ten random rows from the DataFrame df
2. The last ten rows of the DataFrame df
3. The center ten rows of the DataFrame df
4. The top ten rows of the DataFrame df

**Answer:** Option 4: The top ten rows of the DataFrame df

**Explanation:** The `head()` method returns the first n rows of a DataFrame. When given an argument of 10, it returns the first 10 rows. By default (without arguments), it returns 5 rows.

---

# Answer Key
1. Option 2: `DF=pd.DataFrame(data)`
2. Option 4: `df=pd.read_csv(filename)`
3. Option 3: `info()`
4. Option 4: `describe()`
5. Option 4: The top ten rows of the DataFrame df