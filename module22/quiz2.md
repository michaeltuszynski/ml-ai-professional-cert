# CNN Concepts and Techniques Quiz

## Question 1 (1 pt)
Why is fine-tuning a convolutional neural network (CNN) model important?

**Options:**
1. It eliminates the need for data augmentation techniques.
2. It ensures the model is always overfitting to the training data.
3. It helps adjust the model to perform better on a specific task or dataset.
4. It speeds up the training process by using more layers.

**Answer:** Option 3: It helps adjust the model to perform better on a specific task or dataset.

Fine-tuning is the process of taking a pre-trained model and adapting its parameters to a new, specific task or dataset. This technique leverages the general features learned from a large dataset and refines them for a specific application, resulting in better performance while requiring less training data and computational resources.

---

## Question 2 (1 pt)
Which of the following statements is true regarding the pooling layer in convolutional neural networks (CNNs)?

**Options:**
1. The pooling layer in CNNs requires trainable weights for each pooling operation.
2. The pooling layer in CNNs adjusts weights during backpropagation to optimize performance.
3. The pooling layer in CNNs requires zero parameters.
4. The pooling layer in CNNs computes the average of the pixel values in the input feature map.

**Answer:** Option 3: The pooling layer in CNNs requires zero parameters.

Pooling layers perform fixed operations (like max or average) on regions of the input feature maps to reduce dimensions. Unlike convolutional layers, pooling operations don't have any trainable parameters (weights or biases) - they simply apply a deterministic function to summarize the feature information.

---

## Question 3 (1 pt)
What is the technique where you add a bunch of distorted, rescaled, and rotated versions of each image in the training set?

**Options:**
1. Image normalization
2. Feature scaling
3. Dropout regularization
4. Data augmentation

**Answer:** Option 4: Data augmentation.

Data augmentation is a technique that artificially expands the training dataset by creating modified versions of existing data through transformations like rotation, scaling, flipping, and distortion. This helps improve model generalization by exposing it to a wider variety of examples without collecting additional data.

---

## Question 4 (1 pt)
What is the name of the technique which is used to randomly disable connections between some neurons?

**Options:**
1. Dropout
2. Data augmentation
3. Batch normalization
4. Weight regularization

**Answer:** Option 1: Dropout.

Dropout is a regularization technique where randomly selected neurons are temporarily "dropped out" (disabled) during training. This prevents neurons from co-adapting too much and forces the network to learn more robust features, ultimately reducing overfitting and improving generalization.

---

## Answer Key

1. Option 3: It helps adjust the model to perform better on a specific task or dataset. (Utilizing pre-trained knowledge for specific applications)
2. Option 3: The pooling layer in CNNs requires zero parameters. (Pooling uses fixed operations without trainable parameters)
3. Option 4: Data augmentation. (Creating modified versions of training data to improve generalization)
4. Option 1: Dropout. (Randomly disabling neurons during training to prevent overfitting)
