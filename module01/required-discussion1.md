In the previous video, you watched Dr. Gomes work with a number of datasets pulled from various data repositories. Now it is your turn to explore online data repositories that are publicly available. Conduct an Internet search for data repositories in CSV format that are publicly available. Examples of places you could search for datasets are [Kaggle](https://www.kaggle.com) and [Stack Overflow](https://stackoverflow.com).

Select two datasets that are of interest to you. Then, for each dataset you choose, list the following information:

1. A short description of the content of the data
2. One or two possible business uses of the data
3. The location (URL) of the dataset
4. A summary of the characteristics of the dataset using the `describe()` function in pandas

For more details on how to create a Kaggle account, please see the following resource:
[How to Get Started?](https://www.kaggle.com/getting-started)

**Please note:** You will use one of these datasets again later in this module, so please select an appropriately sized dataset for this program and your skill level. A dataset containing ten columns and 500 rows is a good size to start.

**Hint:** If your dataset contains data from many years, you may want to select just one year or a few years to work with later.

---

## Answer

### Dataset 1: Alzheimer's Disease Patient Data

**Description:** This dataset contains the health records of patients who are diagnosed with or are at risk of Alzheimers. Details include demographic data and lifestyle factors.

**Business Case:** By analyzing this data, we could use it to predict who has the highest risk factors of developing Alzheimers.

**Dataset URL:** [Alzheimer's Disease Patient Data on Kaggle](https://www.kaggle.com/datasets/muhammadehsan02/alzheimers-disease-patient-data)

**Summary Statistics:**
```
PatientID    Age         Gender      Ethnicity    EducationLevel
count        2149        2149        2149         2149
mean         5825        74.908795   0.506282     0.697534
std          620.507185  8.990221    0.500077     0.996128
min          4751        60          0            0
25%          5288        67          0            0
50%          5825        75          1            0
75%          6362        83          1            1
max          6899        90          1            3
```

### Dataset 2: Data Science Jobs and Salaries from Indeed

**Description:** This dataset describes data science jobs and salaries. It includes details about job titles, companies, locations, salary ranges, short descriptions, and job links.

**Business Case:** Useful in searching for salary ranges for data science positions currently available.

**Dataset URL:** [Data Science Jobs and Salaries on Kaggle](https://www.kaggle.com/datasets/ritiksharma07/data-science-jobs-and-salaries-indeed)

**Summary Statistics:**
```
count        200
mean         100.5
std          57.879185
min          1
25%          50.75
50%          100.5
75%          150.25
max          200
```