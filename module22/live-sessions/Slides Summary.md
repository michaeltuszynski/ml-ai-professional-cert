# Deep Neural Networks - Office Hours Summary (February 27, 2025)


This document summarizes the key topics discussed during the Deep Neural Networks Office Hours session held by Viviana Márquez on February 27, 2025 [1].


## Agenda


The session covered the following topics [1]:


*   **Capstone meetings and FAQ**

*   **Where have we come from and what do we have left?**

*   **Content review: Deep Neural Networks**

*   **Questions**

*   **Schedule your second 1:1 with your Learning Facilitator** [1]


## Capstone Project


*   **Consultation Sessions:** One 30-minute consultation is available per learner during Modules 21-23 (February 19, 2025 - March 11, 2025) [2].

*   **Learning Facilitator Calendly Links:** Links are provided for scheduling consultations with Vikesh Koul (Section A), Jessica Cervi (Section B), Viviana Márquez (Section C), and Francesca Vera (Section D) [3]. A link is also provided for Mani Kannapan (Section E) [3].

*   **Canvas:** Learners are encouraged to ask for help and know their section on Canvas [2].

*   **Roadmap:** The capstone project has the following milestones [2]:

    *   **Module 6:** Draft the Problem Statement

    *   **Modules 12 to 15:** First 1:1 With Your Learning Facilitator

    *   **Module 16:** Finalizing Your Problem Statement

    *   **Module 20:** Initial Report and EDA

    *   **Modules 21 to 23:** Second 1:1 With Your Learning Facilitator

    *   **Module 24:** Final Analysis and Report


## Program Overview and Deep Learning Modules


*   The program is divided into three content areas [4]:

    *   **Section 1 (Mod 1-5):** Foundations (probability, statistics, data analysis, and code)

    *   **Section 2 (Mod 6-17, 20):** Machine Learning

    *   **Section 3 (Mod 21-24):** NLP, Recommenders, Deep Learning

*   The Deep Learning modules include [4, 5]:

    *   **Mod 21: Deep Neural Networks I:** Foundations of NN, Hyperparameter tuning

    *   **Mod 22: Deep Neural Networks II:** CNNs for image classification, LSTM for time series, FCNN for regression

    *   **Mod 23: GenAI:** GANs, Diffusion models, RNNs to generate text, Transformers to generate text


## AI, Machine Learning, and Deep Learning


*   **Artificial Intelligence (AI)** is a broad field where machines are designed to mimic human intelligence for tasks like decision-making, language understanding, and problem-solving [6]. Its scope is broad, encompassing robotics, NLP, and problem-solving [6].

*   **Machine Learning (ML)** is a subset of AI focused on creating systems that learn and improve from data without explicit programming [7]. Its scope is moderate, including regression, classification, clustering, and ensemble models [7].

*   **Deep Learning (DL)** is a specialized type of machine learning using neural networks with many layers to analyze vast data and learn complex patterns, often achieving human-level performance in areas like image recognition and language translation [7]. Its scope is narrow but powerful [7].


## When to Use Deep Learning vs. Machine Learning


**Deep Learning is suitable when:** [8]


*   There are **large amounts of data**.

*   The data contains **complex patterns**.

*   **High computational power** is available.

*   The problem domain has **proven DL success**.

*   **End-to-end learning** is desired.


**Machine Learning is suitable when:** [8]


*   There is **limited data**.

*   **Interpretability** is important.

*   There is **less computational power**.

*   **Feature engineering** is feasible.

*   **Faster training** is needed.

*   The problem domain has **proven ML success**.


Examples of Deep Learning applications include ChatGPT, Suno AI, Opus Pro, ElevenLabs, and Leonardo AI [8, 9]. Training large DL models like ChatGPT-3 can be very computationally expensive [9].


## GPU vs. CPU for Deep Learning


*   **GPUs (Graphics Processing Units)** are more powerful for certain operations due to their parallel processing capabilities [10]. They have thousands of smaller cores designed for handling multiple computations concurrently, making them adept at matrix operations and floating-point arithmetic common in deep learning [10, 11].

*   **CPUs (Central Processing Units)** have fewer cores and are optimized for sequential processing and general-purpose tasks [11, 12].


## Deep Learning Frameworks


*   **TensorFlow:** An open-source deep learning framework developed by Google, designed for large-scale ML and DL models [12]. Features include eager execution, TensorBoard for visualization, TensorFlow Lite for mobile deployment, and distributed training [13].

*   **Keras:** A user-friendly and modular high-level neural network API that can run on top of TensorFlow, Theano, or CNTK [13, 14]. It allows for easy and fast prototyping and is highly extensible [14]. The `tf.keras` module within TensorFlow is now commonly used [15].

*   **PyTorch:** An open-source deep learning platform developed by Facebook's AI Research lab, known for its flexibility and dynamic computation graphs (Autograd), making it useful for research [15]. It has native Python support, TorchServe for production deployment, and supports distributed training [16].


## Neural Networks


*   A neural network is composed of **neurons** [16].

*   **Artificial Neural Networks (ANNs)** are inspired by biological neural networks [16].

*   **Biological Neuron (Simplified):** Dendrites receive electrical signals, which feed the cell body, and the response is passed through the axon [17].

*   An artificial neuron is called a **Perceptron** [17].

*   A perceptron is a simple form of a neural network and a building block for more complex networks [17].

*   Like any ML model, a perceptron takes **input values** which are then multiplied by **weights** (initialized randomly) [17, 18].

*   The result is passed through an **activation function** (e.g., Positive = 1, Negative = 0) [18].

*   **Bias** is added to avoid mathematical problems and provide flexibility to the model [18].

*   Mathematically, a perceptron is a linear model with an activation function [19, 20].

*   **Artificial Neural Network Parts:**

    *   **Input layer:** Actual data values [19].

    *   **Hidden layers:** Increase the level of abstraction with more layers [19, 21, 22]. The example shows two hidden layers [19].

    *   **Output Layer:** Final estimate [19].

*   NNs send data to a space where everything is **linearly separable** [20, 21].


## Forward Propagation in an ANN


1.  **Initialization:** Weights and biases are initialized with small random values [22]. Bias can be represented as an additional node in each layer (except the output layer) [23]. In PyTorch's `nn.Linear`, bias is automatically added [23].

2.  **Input:** Data is fed into the network [23].

3.  **Forward propagation:** Starting from the input layer, each neuron computes a **weighted sum of its inputs** [24]. This sum is then passed through an **activation function** to produce the neuron's output [24]. This output becomes the input for the next layer, and the process repeats for each subsequent layer [24, 25].


## Activation Functions


*   A mathematical function applied to the output of each neuron [21, 26].

*   Introduces **non-linearity** into the model, allowing the network to represent more complex functions and learn from errors [21, 26].


**Examples of Activation Functions:**


*   **Output Layers:**

    *   **Sigmoid:** Squashes output between 0 and 1 (probability) for binary classification (e.g., email spam detection) [27].

    *   **Softmax:** Outputs a probability distribution over multiple classes for multi-class classification (single label) (e.g., handwritten digit recognition) [27].

    *   **Sigmoid (per neuron):** For multi-label classification (each class is an independent binary classification) (e.g., image tagging) [28].

    *   **Linear or None:** Usually for regression (single or multi-output) (e.g., predicting house prices), but sigmoid or tanh can be used for bounded outputs [28, 29].

    *   **Linear or Others:** For time series forecasting, depending on the range of values (e.g., stock price prediction) [29].

    *   **Linear, Sigmoid, Tanh, etc.:** For autoencoders (dimensionality reduction, denoising) [29].

    *   **Tanh:** Commonly used for the generator's output in generative models like GANs (e.g., generating art images) [30].

    *   **Softmax:** Especially for sequence-to-sequence problems like translation (predicting tokens from a vocabulary) [30, 31].

*   **Hidden Layers:**

    *   **ReLU (Rectified Linear Unit):** f(x) = max(0, x). Pros: Fast to compute, reduces vanishing gradient. Cons: Can suffer from "dead neurons" [26, 31, 32].

    *   **Leaky ReLU:** f(x) = x for x>0 and f(x) = ax for x<=0. Pros: Addresses the "dead neuron" problem of ReLU [31, 32].


**Considerations when choosing activation functions:** [20, 33, 34]


*   **Training Dynamics:** Impact on speed and convergence (e.g., dead neurons).

*   **Computational Considerations:** ReLU is simpler than tanh or sigmoid.

*   **General Rule of Thumb:** ReLU and its variants are often good starting points for feedforward and CNNs.

*   **Problem Nature:** Data distribution and expected relationships (linear/non-linear).

*   **Network Depth:** ReLU and variants are preferred for very deep networks due to the vanishing gradient problem with sigmoid and tanh.

*   **Historical/Previous Success:** What has worked on similar problems.

*   **Experimentation:** Empirical evaluation on validation data is often necessary.


## Training an Artificial Neural Network


1.  **Initialization:** Weights and biases are initialized [22].

2.  **Input:** Training data is fed into the network [23].

3.  **Forward propagation:** Compute the output of the network [24, 25, 35, 36].

4.  **Compute the loss:** Measure the difference between the predicted and target values using a **loss function** (e.g., MSE for regression, Cross-Entropy for classification) [25, 37, 38]. The objective of a neural network is to find weights and biases that minimize this loss function [37, 39-41].

5.  **Backpropagation:** Compute the gradient of the loss function with respect to each weight and bias in the network, indicating how much each parameter contributed to the error [42-44]. This starts from the output layer and moves backward using the chain rule [42, 44].

6.  **Update weights and biases:** Adjust the values of weights and biases using **gradient descent** or its variants (SGD, Adam, etc.) in the direction that minimizes the loss [43, 45, 46]. The update rule for a weight is: `w_new = w_old - α⋅∇_wL`, where α is the learning rate [46].

7.  **Iteration (Epochs):** Repeat steps 3-6 (forward propagation, loss computation, backpropagation, update) until the loss on a validation set stops improving or increases [38, 45]. An **epoch** is one complete forward and backward pass of all training examples [38].

8.  **Evaluation:** Assess the performance of the trained model on unseen data [38].

9.  **Deploy:** Use the trained model for making predictions on new data [38].


## Common Losses in NN


*   **Regression tasks:** **Mean Squared Error (MSE)** calculates the average squared difference between predicted and actual values [38].

*   **Classification tasks:** **Cross-Entropy Loss** measures the difference between the true label distribution and the predicted probability distribution [38].


## Additional Resources


*   Code examples (Tensorflow, PyTorch) [47].

*   Neural Networks by StatQuest [47].

*   PyTorch documentation [47].


## Hyperparameters


*   **Parameters:** Configuration variables internal to the model, learned from training data, and used for predictions (e.g., coefficients in linear regression, support vectors in SVM, split points in a decision tree) [47, 48]. They are often not set manually [48].

*   **Hyperparameters:** Configuration variables set **before** the training process begins, controlling the learning algorithm and the model itself (determining parameters) [49]. They cannot be learned directly from data and are often specified manually [49].


**Examples of Hyperparameters:** [49, 50]


*   **Learning Rate:** Determines the step size for weight updates during gradient descent. Too high can lead to inaccurate convergence, too low can result in slow training or getting stuck in local minima [43, 50].

*   **Regularization Techniques:**

    *   **Dropout Rate:** Prevents overfitting by randomly ignoring some layer outputs during training, making the network less sensitive to specific neuron weights and improving generalization [50, 51].

    *   **L1/L2 Regularization:** Adds a penalty term to the loss function to prevent coefficients from overfitting the training data [51].


## Types of NN


*   **Fully Connected Neural Networks (FCNNs) / Multilayer Perceptrons (MLPs):** Each neuron in one layer is connected to all neurons in the next layer [51-54].

*   **Convolutional Neural Networks (CNNs):** Effective for processing grid-like data such as images, used for computer vision tasks like image recognition and object detection [52, 54-59].

*   **Recurrent Neural Networks (RNNs):** Designed for sequential data (time series, speech, text), maintaining state information ('memory') [60]. Variants include LSTMs and GRUs to handle long-term dependencies and the vanishing gradient problem [60].

*   **Autoencoders (AE):** Used for unsupervised learning tasks, primarily dimensionality reduction and feature learning [60].

*   **Generative Adversarial Networks (GANs):** Consist of a generator and a discriminator trained in a zero-sum game for tasks like generating realistic images [61].

*   **Transformer Networks:** Handle sequential data without recurrence, relying on an 'attention' mechanism. Foundation of models like BERT and GPT [61, 62].


## Convolutional Neural Networks (CNNs)


*   Inspired by the biological processes of the human visual cortex [55].

*   Mimic the visual cortex's hierarchical processing and ability to recognize patterns [55, 56].

*   Use **shared weights** in convolutional filters, leading to **translation invariance** (detecting features regardless of their position) [56, 57].


**Functionality of a CNN:** [57, 58]


*   **Feature Learning:** Initial layers learn basic features (edges, textures), subsequent layers learn more complex features.

*   **Spatial Hierarchy:** Build complex patterns from simpler ones, learning from general to specific.

*   **Translation Invariance:** Recognize learned features anywhere in the image.


**Characteristic Components of a CNN:** [58, 59, 63, 64]


*   **Convolutional Layers:** Apply **filters/kernels** (small weight matrices) that slide over the input image, performing a **convolution operation** (dot product) in local regions (**receptive field**) to produce **feature maps** that emphasize certain features [58, 64-66].

    *   **Stride:** Number of pixels the filter moves across the input [66-68].

    *   **Padding:** Adding pixels (often zeros) around the input to control the output size [66, 67, 69].

    *   **Parameter sharing:** The same filter weights are used across the input [63, 64].

*   **Pooling Layers:** Reduce the spatial size of feature maps (**downsampling**), decreasing parameters and computation, and controlling overfitting [59, 63, 70, 71]. Common operation is **max pooling** [59, 63]. Pooling layers do not have learned weights [70].


## LeNet-5


*   A pioneering CNN developed by Yann LeCun et al., primarily for handwritten digit recognition on the **MNIST dataset** [59, 71-74].

*   Provides an essential historical and architectural perspective [71, 72].

*   **Architecture (Example for MNIST):** [73-78]

    *   **Input Image:** Single-channel (grayscale), 28x28 pixels [73]. Padding can be used to fit expected input size [79].

    *   **First Convolutional Layer:** 5x5 kernel, 2 pixels of padding, 6 filters, sigmoid activation, output 28x28x6 [75].

    *   **First Pooling Layer:** 2x2 kernel, average pooling, stride 2, output 14x14x6 [75].

    *   **Second Convolutional Layer:** 5x5 kernel, no padding, 16 filters, sigmoid activation, output 10x10x16 (assuming stride 1) [76].

    *   **Second Pooling Layer:** 2x2 kernel, average pooling, stride 2, output 5x5x16 [77].

    *   **Flatten:** The pooled feature maps are flattened into a single vector [77].

    *   **First Fully Connected Layer:** 120 neurons, sigmoid activation [77, 78].

    *   **Second Fully Connected Layer:** 84 neurons, sigmoid activation [78].

    *   **Output Fully Connected Layer:** 10 neurons (for 10 classes), typically softmax activation to output a probability distribution [74, 78].

    *   **Output:** Probability distribution across the 10 classes [74].


## Other CNN Architectures


*   **AlexNet:** Deeper and wider than LeNet, introduced ReLU activations, won ImageNet in 2012 [72, 80, 81].

*   **VGGNet:** Known for its simplicity, using only stacked 3x3 convolutional layers [80, 82].

*   **GoogLeNet (Inception):** Introduced the inception module with multiple filter sizes, reduced parameters [80, 83].

*   **ResNet (Residual Network):** Introduced residual connections to allow training of very deep networks [81, 83].

*   **U-Net:** Designed for biomedical image segmentation, with contracting and expanding paths [83].

*   **DenseNet (Densely Connected Convolutional Networks):** Each layer connects to every other layer in a feed-forward fashion, known for parameter efficiency [83, 84].


## ImageNet


*   A large-scale, diverse database of over 14 million hand-annotated images, influential in computer vision and deep learning research [65, 74, 81, 84].

*   Provides a standard dataset for training and testing algorithms [65].

*   **Pre-trained models on ImageNet** are widely used for **transfer learning**, adapting a model trained on a large dataset to a smaller, domain-specific dataset [65, 81, 85]. **Don't start a new network from scratch; use pre-trained models** [81, 85].


## Gradient Descent


*   An optimization algorithm to find the minimum of the loss function (objective of a neural network) by iteratively adjusting weights and biases [39-41, 46].

*   The **gradient** of the loss indicates the direction of the steepest increase [40, 41]. Gradient descent moves in the **opposite direction** (steepest descent) to minimize the loss [46].

*   The **learning rate (α)** is a hyperparameter determining the step size in each iteration [43, 46].


**Types of Gradient Descent:** [86, 87]


*   **Batch Gradient Descent:** Uses the entire dataset for each gradient computation (computationally expensive for large datasets).

*   **Stochastic Gradient Descent (SGD):** Uses one example per iteration (faster, can escape local minima, but noisy).

*   **Mini-Batch Gradient Descent:** Uses a small random sample (most common in deep learning).

*   **Adam (Adaptive Moment Estimation):** Often preferred over simple mini-batch GD due to adaptive learning rates, momentum, and bias correction [87].


**Avoiding Local Minima:** Strategies include using momentum-based optimizers, adaptive learning rates, SGD, random restarts, etc. [79, 87].


## Backpropagation


*   Computes the gradient of the loss with respect to each weight and bias in the network [43, 44].

*   Starts from the output layer and moves backward, applying the chain rule [43, 44].

*   Deep learning frameworks like TensorFlow and PyTorch handle this automatically [44, 86].


## CNN Layers Learn


*   **Early layers:** Learn basic feature detection filters (edges, corners) [68].

*   **Middle layers:** Learn filters that detect parts of objects (e.g., eyes, noses for faces) [68].

*   **Last layers:** Learn higher representations, recognizing full objects in different shapes and positions [68].


## BONUS | Grad-CAM


*   **Gradient-weighted Class Activation Mapping:** A technique to make CNN models more transparent by visualizing the input regions important for predictions [85, 88].

*   Helps understand which parts of an image lead the CNN to its classification decision [85, 88].


## Code - CNN


Links to Google Colab notebooks providing practical examples: [39, 88]


*   Intro to computer vision

*   LeNet5

*   Pre-trained ResNet (Transfer learning)

*   GradCAM

*   ResNet with hyperparameter tuning