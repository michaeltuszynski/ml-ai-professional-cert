# Module 4 Quiz

## Question 1 (1 point)
What is the correct statement to rename a column named Code to Country in DataFrame df?

**Options:**
1. `df.rename(columns ={"Code" "Country"})`
2. `df.rename(columns ={"Code" : "Country"})`
3. `df.rename(columns ={Code : Country})`
4. `df.rename(columns ="Code" : "Country")`

**Answer:** Option 2: `df.rename(columns ={"Code" : "Country"})`

*Explanation:* The correct syntax for renaming columns in pandas uses a dictionary with the format `{old_name : new_name}`. The keys and values must be strings and properly quoted, with a colon separator.

## Question 2 (1 point)
Given two DataFrames (df1 and df2) with common Entity columns, what will the Python statement for joining them into a new DataFrame (df3) be?

**Options:**
1. `df3=pd.merge(left=df1, right=df2, left_on="Entity")`
2. `df3=pd.merge(left=df1, right=df2, right_on="Entity")`
3. `df=pd.merge(left = df1, right=df2, key =Entity)`
4. `df3=pd.merge(left=df1, right=df2, left_on="Entity",right_on="Entity")`

**Answer:** Option 4: `df3=pd.merge(left=df1, right=df2, left_on="Entity",right_on="Entity")`

*Explanation:* When merging DataFrames on a common column, you need to specify both `left_on` and `right_on` parameters to indicate the matching columns from each DataFrame.

## Question 3 (1 point)
The function merge() is used to join two datasets into one. Which constructor is used to declare the type of join?

**Options:**
1. `key`
2. `right_index`
3. `left`
4. `how`

**Answer:** Option 4: `how`

*Explanation:* The `how` parameter in pandas merge() specifies the type of join to perform (e.g., 'inner', 'outer', 'left', 'right').

## Question 4 (1 point)
What is the type of join where the resulting table contains only rows from both tables where the joining condition is met?

**Options:**
1. Cross join
2. Outer join
3. Inner join
4. Left join

**Answer:** Option 3: Inner join

*Explanation:* An inner join returns only the rows where there are matching values in both tables, effectively keeping only the intersection of the two datasets.

---

# Answer Key
1. Option 2 - `df.rename(columns ={"Code" : "Country"})` (Proper dictionary syntax for column renaming)
2. Option 4 - `df3=pd.merge(left=df1, right=df2, left_on="Entity",right_on="Entity")` (Complete merge syntax specifying both join columns)
3. Option 4 - `how` (Parameter that specifies join type)
4. Option 3 - Inner join (Returns only matching rows between tables)