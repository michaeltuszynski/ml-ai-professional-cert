# Overview: Gradient Descent Basics

In ML, a kernel is a method of solving a nonlinear problem using a linear classifier. This involves separating linearly inseparable data (as shown as Figure 1) from linearly separable data (as shown as Figure 2). In each data instance, a kernel function maps the original nonlinear observations to a higher-dimensional space that can be separated.

![Linearly Inseparable Data](<images/bh-pcmlai 16.1.png>)

![Linearly Separable Data](<images/bh-pcmlai 16.2.png>)

Now that you understand the kernel, the kernel trick will be easier to understand. The kernel trick allows you to find a decision surface that differentiates between different classes if the data can be mapped from two-dimensional space to three-dimensional space. Then, as dimensional computations become more expensive within those spaces, the kernel can use the data in the original feature space without requiring coordinates in a higher-dimensional space.