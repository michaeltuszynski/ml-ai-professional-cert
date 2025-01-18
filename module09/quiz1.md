# Module 9 Quiz

## Question 1 (1 point)
If a dataframe has two columns, "horsepower" and "weight," then the output of a polynomial features object with degree two will have which features?

**Options:**
1. ["hp", "weight", "hp^2", "hp weight", "weight^2"]
2. ["hp", "weight", "hp", "hp weight"]
3. ["hp", "weight", "hp^2", "weight^2"]
4. ["hp", "weight"]

**Answer:** Option 1: ["hp", "weight", "hp^2", "hp weight", "weight^2"]

*Explanation:* A polynomial features transformation of degree 2 generates all possible combinations of features up to degree 2. This includes:
- Original features (hp, weight)
- Squared terms (hp^2, weight^2)
- Interaction terms (hp×weight)

---

## Question 2 (1 point)
What is the result of increasing the degree parameter of the polynomial features on multidimensional data?

**Options:**
1. The number of polynomial features first decreases, then increases
2. The number of polynomial features decreases
3. The number of polynomial features remains the same
4. The number of polynomial features increases

**Answer:** Option 4: The number of polynomial features increases

*Explanation:* Increasing the polynomial degree generates additional higher-order terms and interactions, which always results in more features being created.

---

## Question 3 (1 point)
A given dataframe has two columns: "horsepower" and "weight." How many features will a polynomial object of degree 3 have?

**Options:**
1. 2
2. 10
3. 5
4. 9

**Answer:** Option 4: 9

*Explanation:* With 2 features and degree 3, you get:
- Original features (2): hp, weight
- Degree 2 terms (3): hp^2, hp×weight, weight^2
- Degree 3 terms (4): hp^3, hp^2×weight, hp×weight^2, weight^3
Total: 2 + 3 + 4 = 9 features

---

## Answer Key
1. Option 1 - Complete polynomial features of degree 2 (includes original, squared, and interaction terms)
2. Option 4 - Increasing polynomial degree always increases feature count
3. Option 4 - 9 features total for 2 input features with degree 3 (2 original + 3 degree-2 terms + 4 degree-3 terms)