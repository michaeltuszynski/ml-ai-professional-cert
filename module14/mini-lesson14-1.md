# Mini-Lesson 14.1: Decision Trees and Their Components

Decision trees are tree-like structures that can classify data. The decision tree decomposes the data into subtrees composed of leaf nodes.

## Types of Nodes

There are three types of nodes in a decision tree:

- **Root node**: The beginning of the tree
- **Internal nodes**: Nodes that have two or more branches and can be split further into additional nodes
- **Leaf nodes**: The lowest nodes that can no longer be split

## Steps to Build a Decision Tree

### Step 1: Determine the tree's root node
The root node is the starting point of the decision tree. It represents the entire dataset. To determine the root node, choose the attribute that best splits the data into subsets with the highest information gain or lowest impurity (e.g., Gini impurity or entropy).

**Example**: Suppose you have a dataset of customer information, and you want to predict whether a customer will buy a product (yes/no). The attribute "Income" might be a good choice for the root node.

### Step 2: Calculate the class entropy
Entropy measures the impurity or disorder in a dataset. For a binary classification problem (e.g., yes/no), the class entropy is calculated as:

```
E(S) = −p+​log2​(p+​) – p−​log2​(p−​)
```

where (p+) and (p−) are the proportions of positive and negative examples in the dataset.

**Example**: If your dataset has 80% positive (buy) and 20% negative (not buy) examples, the class entropy would be:

```
E(S) = −0.8log2​(0.8) − 0.2log2​(0.2) ≈ 0.72
```

### Step 3: Calculate the entropy for each attribute after splitting
For each attribute, calculate the entropy after splitting the data based on that attribute. The attribute with the lowest post-split entropy is chosen.

**Example**: If you split the dataset by "Income," you calculate the entropy for high-income and low-income groups separately.

### Step 4: Calculate the information gain on each split
Information gain measures how much the entropy decreases after splitting by an attribute. It is calculated as the difference between the original entropy and the weighted average of post-split entropies.

**Example**: If splitting by "Income" reduces entropy significantly, it has high information gain.

### Step 5: Perform the split
Based on information gain, choose the attribute with the highest gain, and split the dataset.

**Example**: If "Income" provides the highest gain, you create child nodes for high-income and low-income groups.

### Step 6: Perform further splits
Repeat steps 3–5 for each child node, recursively creating subtrees.

**Example**: For the high-income group, you might split further based on "Age" or "Education."

### Step 7: Complete the decision tree
Continue splitting until a stopping criterion (e.g., maximum depth or minimum samples per leaf) is met.

**Example**: Your decision tree might have branches such as "High Income -> Age > 30 -> Buy" or "Low Income -> Education = High School -> Not Buy."

### Step 8: Assess the accuracy of the decision tree
Use a validation dataset to evaluate the tree's performance (e.g., accuracy, precision, recall).

**Example**: You can use a decision tree to visualize new customer data to see how well it predicts their buying behavior.

## Reference Diagram
![alt text](<images/bh-pcmlai 14.1.png>)

---
Source: Java Tpoint. "Decision Tree Classification Algorithm." Accessed July 26, 2024. [https://www.javatpoint.com/machine-learning-decision-tree-classification-algorithm](https://www.javatpoint.com/machine-learning-decision-tree-classification-algorithm)