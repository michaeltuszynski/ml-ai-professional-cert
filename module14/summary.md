# Module 14: Decision Trees - Comprehensive Summary

## Video 1: Introduction
### Main Topic
- Introduction to decision trees as a classification algorithm

### Key Concepts
- Decision trees are sequences of questions leading to classifications
- Questions are answered in sequence to yield predictions
- Each node represents a decision point

### Practical Example
- Animal classification example:
  - Number of legs (0 → Snake, 4 → further questions)
  - Does it purr? (Yes → Cat, No → Dog)
  - For 2 legs: Additional questions for Kangaroo, Human, or Parrot

### Dataset Introduction
- Iris flower dataset:
  - 150 flower measurements
  - Three species: Versicolor, Setosa, Virginica
  - Features: sepal_length, sepal_width, petal_length, petal_width

## Video 2: Building Decision Trees Visually
### Main Topic
- Manual construction of decision trees

### Process
1. Start with visual data analysis
2. Identify clear separations in data
3. Create rules based on feature thresholds

### Example Rules
1. Setosa identification:
   - petal_width < 0.75 AND petal_length < 2
2. Virginica identification:
   - petal_width ≥ 1.75
3. Further refinements for remaining classifications

### Key Points
- Multiple valid rules possible for same separation
- Rules can be simple or complex
- Training error consideration important

## Video 3: Building Decision Trees in Scikit-learn
### Implementation Details
- Using DecisionTreeClassifier
```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X, y)
```

### Visualization Tools
1. Basic visualization: `plot_tree`
2. Advanced visualization: `export_graphviz` with Graphviz

### Node Information
- Questions/rules at each node
- Sample counts
- Class distributions
- Entropy values
- Majority class predictions

## Video 4: Measuring Decision Tree's Training Error
### Key Concepts
- Training accuracy analysis
- Impure nodes concept
- Feature overlap challenges

### Technical Details
- Perfect accuracy except when samples have identical features
- Handling overlapping data points
- Query method for analyzing decision paths

## Video 5: Decision Tree Overfitting
### Main Topics
- Overfitting identification
- Complex boundary formation
- Feature impact on overfitting

### Warning Signs
- Erratic decision boundaries
- Personal bubbles for individual points
- Deep, complex tree structures
- Small sample counts in leaves

### Key Insight
- More features don't necessarily lead to overfitting
- Feature relevance matters more than quantity

## Video 6: Decision Tree Boundaries
### Algorithm Overview
1. Start at root node
2. Select best feature and split value
3. Split data into two nodes
4. Repeat until nodes are pure or unsplittable

### Key Terms
- Pure node: Contains samples from only one class
- Unsplittable node: Has overlapping data from different classes

## Video 7: Entropy
### Technical Concept
- Entropy (S) calculation:
  ```
  S = -Σ(p_C * log2(p_C))
  ```
  where p_C is proportion of class C in node

### Properties
- Zero entropy: All samples in same class
- Entropy = 1: Even split between two classes
- Entropy = 1.58: Even split between three classes
- Maximum entropy = log2(C) for C classes

## Video 8: Using Entropy for Tree Selection
### Decision Process
1. Calculate weighted entropy (WS)
2. Compute entropy reduction (ΔWS)
3. Select splits with largest ΔWS

### Technical Details
- WS = entropy * (node_samples/total_samples)
- ΔWS must be positive
- Higher ΔWS indicates better splits

## Video 9: Restricting Tree Complexity
### Hyperparameters
1. min_sample_split: Minimum samples for node splitting
2. max_depth: Maximum tree depth
3. min_impurity_decrease: Minimum required ΔWS

### Pruning Strategies
- Post-growth branch removal
- Validation set-based pruning
- Most common prediction substitution

## Video 10: Model Evaluation vs Humans
### Case Study: Bail Decisions
- Comparing algorithmic vs human judge decisions
- Data requirements and limitations
- Evaluation methodology

### Key Findings
- Algorithm achieved either:
  - 10% crime reduction with 2% more jailing
  - 20% crime reduction with 7% more jailing

### Evaluation Methods
- Random judge assignment
- Comparison with lenient judges
- Efficiency metrics

## Video 11: Conclusion
### Key Takeaways
1. Decision trees are highly interpretable
2. Can achieve 100% training accuracy
3. Require careful overfitting prevention
4. Multiple complexity control methods available

### Advantages
- Easy to understand and execute
- No complex arithmetic needed
- Suitable for various data types

### Limitations
- Tendency to overfit
- Less elegant regularization
- May require pruning

### Tools & Technologies
- Scikit-learn
- Graphviz
- Python libraries for visualization