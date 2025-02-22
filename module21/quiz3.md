# Machine Learning Classification Quiz

## Question 1 (1 point)
What is a binary classification problem in machine learning?

**Options:**
1. A problem where the goal is to predict a continuous value based on input data
2. A problem where the goal is to group data into clusters without predefined labels
3. A problem where the goal is to classify data into more than two categories
4. A problem where the goal is to classify data into exactly two categories

**Answer:** Option 4: A problem where the goal is to classify data into exactly two categories

*Explanation:* A binary classification problem is fundamentally defined as a task where the output can only be one of two possible classes. Common examples include spam detection (spam/not spam), medical diagnosis (positive/negative), or fraud detection (fraudulent/legitimate). This is distinct from regression (continuous values), clustering (unsupervised grouping), and multiclass classification (more than two categories).

---

## Question 2 (1 point)
In a multiclass classification problem where you have four distinct classes, how many nodes should be present in the output layer if you are using a softmax activation function?

**Options:**
1. Two nodes
2. Four nodes
3. One node
4. Three nodes

**Answer:** Option 2: Four nodes

*Explanation:* When using softmax activation for multiclass classification, the number of nodes in the output layer must match the number of possible classes. Each node represents the probability of the input belonging to that specific class, and the softmax function ensures these probabilities sum to 1. For four distinct classes, you need exactly four output nodes to represent the probability distribution across all possible classes.

---

## Question 3 (1 point)
Which of the following statements is true regarding the softmax function in relation to its output values?

**Options:**
1. If xi = xj, then yi > yj
2. If xi > xj, then yi < yj
3. If xi < xj, then yi < yj
4. If xi > xj, then yi > yj

**Answer:** Option 3: If xi < xj, then yi < yj

*Explanation:* The softmax function maintains monotonicity, meaning that if an input value (xi) is less than another input value (xj), its corresponding output probability (yi) will also be less than the other output probability (yj). This preserves the relative ordering of inputs in the output probabilities - larger input values result in larger probabilities, and smaller input values result in smaller probabilities. This is a fundamental property that makes softmax suitable for converting neural network logits into meaningful probability distributions.

---

## Question 4 (1 point)
What is the loss function for building a neural network that uses integer encoding?

**Options:**
1. categorical_sparse_entropy
2. categorical_sparse_crossentropy
3. categorical_crossentropy
4. sparse_categorical_crossentropy

**Answer:** Option 4: sparse_categorical_crossentropy

*Explanation:* When using integer encoding (where class labels are represented as integers) in neural networks, the appropriate loss function is sparse_categorical_crossentropy. This loss function is specifically designed to work with integer-encoded labels, unlike categorical_crossentropy which expects one-hot encoded labels. The "sparse" in the name indicates that the target labels are provided as integers rather than one-hot vectors.

---

# Answer Key

1. Option 4 - Binary classification (Classifying data into exactly two categories)
2. Option 2 - Four nodes (Matching number of output nodes to number of classes)
3. Option 3 - If xi < xj, then yi < yj (Monotonicity property of softmax: smaller inputs yield smaller probabilities)
4. Option 4 - sparse_categorical_crossentropy (Loss function for integer-encoded labels)