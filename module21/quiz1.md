# Computer Vision and Deep Learning Quiz

## Question 1 (1 point)
What does the acronym HoG stand for in the context of computer vision and deep learning?

**Options:**
1. Histogram of oriented gradients
2. High-level object gradient
3. Histogram of optical gradients
4. Histogram of oblique gradients

**Answer:** Option 1: Histogram of oriented gradients

**Explanation:** HoG (Histogram of Oriented Gradients) is a feature descriptor technique used in computer vision and image processing for object detection. It works by analyzing the distribution of edge orientations within an object to describe its shape and appearance. The technique counts occurrences of gradient orientation in localized portions of an image, making it particularly effective for object detection and recognition tasks.

## Question 2 (1 point)
What is the standard benchmark for comparison of preprocessing techniques and algorithms for image classification?

**Options:**
1. GraphNet
2. ImageClass
3. ImageLabel
4. ImageNet

**Answer:** Option 4: ImageNet

**Explanation:** ImageNet is the first and most important large-scale open-source dataset widely used for benchmarking deep learning algorithms in computer vision. It contains over 14 million annotated images and has become the de facto standard for comparing preprocessing techniques and algorithms for image classification. Its extensive database and standardized evaluation metrics make it an essential tool for measuring progress in computer vision tasks.

## Question 3 (1 point)
Which of the following is not an activation function for neural networks?

**Options:**
1. ReLU: Φ(x)=max(0,x)
2. Tanh: Φ(x)=e2x−1/e2x+1
3. Sigmoid: Φ(x)=1/1+e−x
4. TanU: Φ(x)=max(x,0)

**Answer:** Option 4: TanU: Φ(x)=max(x,0)

**Explanation:** TanU is not a real activation function used in neural networks. The standard activation functions include ReLU (Rectified Linear Unit), Tanh (Hyperbolic Tangent), and Sigmoid, each serving specific purposes in neural network architectures. The formula given for TanU appears to be a variation of ReLU, but it is not a recognized activation function in the field.

## Question 4 (1 point)
What effect does adding a sigmoid activation function to the output node of a regression model have?

**Options:**
1. It changes the model to predict values in the range [-1, 1]
2. It allows the model to handle multi-class classification problems
3. It converts the model into a binary classification model with output values between 0 and 1
4. It increases the output range to cover both positive and negative infinity

**Answer:** Option 3: It converts the model into a binary classification model with output values between 0 and 1

**Explanation:** The sigmoid activation function transforms any input into an output between 0 and 1, following the formula f(x) = 1/(1 + e^(-x)). When added to the output node of a regression model, it effectively converts the model into a binary classifier since all outputs are compressed into the [0,1] range, making it suitable for binary classification tasks where probabilities are desired.

---

## Answer Key
1. Option 1: Histogram of oriented gradients (Feature descriptor for object detection in computer vision)
2. Option 4: ImageNet (Standard large-scale dataset for benchmarking image classification)
3. Option 4: TanU (Not a real activation function)
4. Option 3: Converts to binary classification with [0,1] range (Sigmoid compresses outputs to probability-like values)