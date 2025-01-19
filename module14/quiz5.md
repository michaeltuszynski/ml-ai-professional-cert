## Decision Trees Quiz

### Question 1 (1 pt)
In the decision tree algorithm, after selecting the best feature "x" and the best split value "β," the data is split into two nodes. One of the nodes has a rule that x < β. What is the rule for the other node?

1. x >= 0
2. x = β
3. x >= β
4. x > β

**Correct Answer: 3 (x >= β)**

**Explanation:** In decision trees, when we split on a continuous variable, we create two mutually exclusive and exhaustive groups. If one node contains all samples where x < β, then the other node must contain all remaining samples where x >= β. This ensures that every sample is classified into exactly one node and no samples are left out.

### Question 2 (1 pt)
Here is a node from a decision tree:

```
sepal_length ≤ 5.45
gini = 0.665
samples = 110
value = [34, 36, 40]
class = virginica
```

If the value corresponds to the three species of iris flower, given as p0,p1 and p2, what would be the value of p2?

1. 0.309
2. 0.35
3. 0.36
4. 0.327

**Correct Answer: 3 (0.36)**

**Explanation:** To find p2, we need to calculate the proportion of the third class (40) relative to the total samples. The value array [34, 36, 40] sums to 110 total samples. Therefore, p2 = 40/110 = 0.36 or 36%.

### Question 3 (1 pt)
What is the entropy (S) for a node with p values of ["p0=0.31," "p1=0.33," "p2=0.36"]?

1. 2.5
2. 0
3. 1
4. 1.58

**Correct Answer: 4 (1.58)**

**Explanation:** The entropy formula for multiple classes is: S = -Σ(pi * log2(pi)). When we calculate this for the given probabilities:
- -0.31 * log2(0.31)
- -0.33 * log2(0.33)
- -0.36 * log2(0.36)
The sum gives us approximately 1.58, which represents high entropy (uncertainty) as the classes are fairly evenly distributed.