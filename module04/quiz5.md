# Quiz 5: String Operations in Pandas

## Question 1 (1 point)
Which statement would return rows only for entities that start with "F"?

**Options:**
1. `df1[df1["Entities"].str.startswith("F")]`
2. `df1[df1["Entities"].startswith("F")]`
3. `df1[df1[Entities].str.startswith("F")]`
4. `df1[df1[Entities].str.startswith("F")]`

**Answer:** Option 1: `df1[df1["Entities"].str.startswith("F")]`
- Core definition: The `.str` accessor is required to apply string operations on pandas Series
- Implementation detail: Double quotes are used to properly reference the column name "Entities"

---

## Question 2 (1 point)
Which function is used to replace a string value?

**Options:**
1. `str.replace()`
2. `replaces()`
3. `str.replaced()`
4. `replace[]`

**Answer:** Option 1: `str.replace()`
- Core definition: `str.replace()` is the standard string method for replacing substrings
- Implementation detail: The method takes the search string and replacement string as arguments

---

## Question 3 (1 point)
Which of the following statements is used to replace the first two occurrences of 'o' with 'x' in the string 'book'?

**Options:**
1. `'book'.replace('o', 'x')`
2. `'book'.replace('o', 'x', 1)`
3. `'book'.replace('o', 'x', 2)`
4. `'book'.replace('o', 'x', count=2)`

**Answer:** Option 3: `'book'.replace('o', 'x', 2)`
- Core definition: The third parameter in `replace()` specifies the maximum number of replacements
- Implementation detail: The value 2 indicates that only the first two occurrences will be replaced

---

## Answer Key
1. Option 1: `df1[df1["Entities"].str.startswith("F")]` (Uses proper pandas string accessor)
2. Option 1: `str.replace()` (Standard string replacement method)
3. Option 3: `'book'.replace('o', 'x', 2)` (Limits replacements to first two occurrences)