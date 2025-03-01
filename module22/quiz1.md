# Module 22 Quiz

## Question 1 (1 pt)
What is the following concept called?
"If all of the neighbors of a particular pixel are white, then it is likely that the pixel itself is also white."

**Options:**
1. Feature matching
2. Image segmentation
3. Pixel homogeneity
4. Spatial correlation

**Answer:** Option 4: Spatial correlation
Spatial correlation refers to the statistical relationship between pixels that are near each other in an image. The concept describes how neighboring pixels tend to have similar values due to the continuous nature of most real-world surfaces and objects. This principle is fundamental to many image processing algorithms.

## Question 2 (1 pt)
In a convolutional neural network (CNN), which component is responsible for introducing nonlinearity into the model's output after applying a convolutional filter to the input data?

**Options:**
1. Activation function
2. Kernel
3. Bias
4. Pooling layer

**Answer:** Option 1: Activation function
Activation functions apply a non-linear transformation to the output of a convolutional layer. Without activation functions, the neural network would only be capable of learning linear relationships regardless of depth. Common activation functions in CNNs include ReLU, sigmoid, and tanh.

## Question 3 (1 pt)
The max pooling operation in a convolutional neural network (CNN) takes a feature map as input and produces another feature map of reduced size. Which of the following statements best describes the max pooling operation?

**Options:**
1. It applies a convolutional filter to the feature map to detect edges.
2. It averages all pixel values in a specified region of the feature map.
3. It adjusts the weights of the neurons in the fully connected layers.
4. It retains the maximum pixel value from a specified region of the feature map.

**Answer:** Option 4: It retains the maximum pixel value from a specified region of the feature map.
Max pooling is a downsampling operation that reduces the spatial dimensions of a feature map by selecting the maximum value within defined regions (typically 2×2 windows). This helps achieve spatial invariance to small translations and reduces computational complexity.

## Question 4 (1 pt)
Which of the following is NOT a part of specifying a convolution layer in Keras?

**Options:**
1. Flatten and softmax
2. Specifying the number of filters
3. Size of the kernel
4. Activation function

**Answer:** Option 1: Flatten and softmax
When specifying a convolution layer in Keras, you define parameters like number of filters, kernel size, and activation function. Flatten and softmax are not part of convolution layer specification - flatten is used to transform multi-dimensional outputs into a 1D vector, and softmax is typically used as an activation function in the final layer for classification tasks.

---

## Answer Key

1. Option 4: Spatial correlation (describes the statistical relationship between neighboring pixels)
2. Option 1: Activation function (introduces nonlinearity after applying convolution)
3. Option 4: It retains the maximum pixel value from a specified region of the feature map (defines max pooling operation)
4. Option 1: Flatten and softmax (not part of convolution layer specification)
