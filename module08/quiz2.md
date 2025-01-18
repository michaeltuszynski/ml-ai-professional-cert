# Quiz 2: Polynomial Features and Statistical Modeling

## Question 1 (1 point)
Which of the following statements regarding the PolynomialFeatures class from the sklearn.preprocessing module is correct?

**Options:**
1. PolynomialFeatures generates polynomial and interaction features for the input data.
2. This class is specifically designed for handling missing values within a dataset before model training.
3. It is primarily utilized for scaling numerical features within a dataset to improve model performance.
4. PolynomialFeatures is used for reducing the dimensionality of a dataset by transforming it into a polynomial feature space.

**Answer:** Option 1: PolynomialFeatures generates polynomial and interaction features for the input data.

*Explanation:* PolynomialFeatures is a transformer class that creates new features by computing polynomial combinations of the input features up to a specified degree. This is its core functionality, distinct from data preprocessing tasks like handling missing values or feature scaling.

---

## Question 2 (1 point)
Which of the following best describes the purpose of the degree term in the PolynomialFeatures class?

**Options:**
1. It determines the minimum degree of the polynomial features to be included in the transformation.
2. It controls the regularization strength applied to the polynomial features during model training.
3. It indicates the number of interaction terms to be created between the original features.
4. It specifies the maximum degree of the polynomial features to be generated.

**Answer:** Option 4: It specifies the maximum degree of the polynomial features to be generated.

*Explanation:* The degree parameter in PolynomialFeatures sets the highest degree of polynomial features to be created. For example, with degree=2, it generates features up to and including quadratic terms (x²) and their interactions.

---

## Question 3 (1 point)
Which of the following statements accurately describes the process of fitting and transforming data using the PolynomialFeatures transformer?

**Options:**
1. Both fitting and transforming involve analyzing the data to determine the number and names of the output features, with transforming additionally calculating the actual values of the polynomial features.
2. Fitting determines the number and names of the output features, while transforming calculates the actual values of the polynomial features.
3. Fitting involves calculating the actual values of the polynomial features, while transforming determines the number and names of the output features.
4. Fitting and transforming both involve generating polynomial features based on the degree specified, with fitting focusing on new data and transforming on the original dataset.

**Answer:** Option 2: Fitting determines the number and names of the output features, while transforming calculates the actual values of the polynomial features.

*Explanation:* In scikit-learn transformers, the fit step analyzes the input data structure to determine the feature names and output shape, while transform applies the actual polynomial feature computation to create new features.

---

## Question 4 (1 point)
Which of the following statements best describes the difference between prediction and inference in the context of statistical modeling?

**Options:**
1. Prediction is about understanding the relationship between the response and predictor variables, while inference involves estimating the value of the response variable based on predictor variables.
2. Prediction is used to conclude something about the present, while inference always pertains to estimating future events or occurrences.
3. Prediction and inference are two terms with identical meanings; they both refer to estimating future events or occurrences based on past data.
4. Prediction focuses on estimating the value of the response variable based on predictor variables, while inference emphasizes understanding the relationship between the response and predictor variables.

**Answer:** Option 4: Prediction focuses on estimating the value of the response variable based on predictor variables, while inference emphasizes understanding the relationship between the response and predictor variables.

*Explanation:* The key distinction is in their primary goals: prediction aims to estimate specific outcomes, while inference seeks to understand the underlying relationships and patterns in the data.

---

## Answer Key
1. Option 1 - PolynomialFeatures generates polynomial and interaction features (Core functionality of the transformer)
2. Option 4 - Specifies the maximum degree of polynomial features (Parameter definition)
3. Option 2 - Fit determines feature structure, transform computes values (Transformer workflow)
4. Option 4 - Prediction estimates values, inference understands relationships (Statistical concepts)