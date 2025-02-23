# Module 21 Quiz 4: Neural Networks

## Question 1 (1 pt)
Which of the following terms refers to the number of neurons in each layer of a neural network?

**Options:**
1. Depth
2. Epochs
3. Width
4. Batch size

**Answer:** Option 3: Width
- Core definition: Width in neural networks specifically refers to the number of neurons in each layer
- Context: This is distinct from depth (number of layers) and other parameters like epochs or batch size that relate to training

---

## Question 2 (1 pt)
What tool is used to select hyperparameters for neural networks?

**Options:**
1. Regression
2. Cross-validation
3. Loss function
4. Accuracy

**Answer:** Option 2: Cross-validation
- Core definition: Cross-validation is the primary tool used to evaluate and select optimal hyperparameters for neural networks
- Context: From the summary, cross-validation guides architecture choices and helps monitor overfitting while comparing multiple model configurations

---

## Question 3 (1 pt)
When using cross-validation on neural networks, which model is typically chosen based on the cross-entropy loss on the development set?

**Options:**
1. The model with the lowest cross-entropy loss
2. The model with the average cross-entropy loss
3. The model with the highest cross-entropy loss
4. The model with the most complex architecture

**Answer:** Option 1: The model with the lowest cross-entropy loss
- Core definition: The model with the lowest cross-entropy loss on the development set is selected as it indicates better performance
- Context: This aligns with the best practices mentioned in the hyperparameter tuning section where validation sets are used to monitor and select the best performing model

---

## Question 4 (1 pt)
Which tool in Keras is used to search a predefined set of hyperparameters?

**Options:**
1. TunerBoard
2. Keras Optimizer
3. KerasTuner
4. Keras Callbacks

**Answer:** Option 3: KerasTuner
- Core definition: KerasTuner is the dedicated tool in Keras for automated hyperparameter search
- Context: As mentioned in the summary's hyperparameter tuning section, Keras Tuner is one of the primary tools for comparing and selecting optimal model configurations

---

## Question 5 (1 pt)
What is the algorithm that computes the gradients in small steps called?

**Options:**
1. Mini-step
2. Small-batch
3. Mini-chunk
4. Mini-batch

**Answer:** Option 4: Mini-batch
- Core definition: Mini-batch is the algorithm that processes data in small batches to compute gradients during training
- Context: From the summary's batch gradients section, mini-batch computation is used for gradient approximation with a default batch size of 32

---

## Question 6 (1 pt)
What are batch losses?

**Options:**
1. An array that stores loss values after every batch
2. An array that stores average loss values
3. The average loss of all batches
4. An array that stores overall loss values

**Answer:** Option 1: An array that stores loss values after every batch
- Core definition: Batch losses are the individual loss values computed and stored after processing each batch during training
- Context: As described in the Computing Batch Gradients section, these values are tracked separately from epoch losses and help monitor training progress

---

## Answer Key
1. Option 3: Width (defines number of neurons per layer)
2. Option 2: Cross-validation (tool for hyperparameter selection)
3. Option 1: Lowest cross-entropy loss (optimal model selection criterion)
4. Option 3: KerasTuner (Keras' hyperparameter search tool)
5. Option 4: Mini-batch (gradient computation method)
6. Option 1: Array of batch loss values (training progress tracking)