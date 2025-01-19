# Overview: Two-Dimensional Gradient Descent

One-dimensional gradient descent is straightforward because it passes one over two or three dimensions to the objective function. Therefore, to solve more complex problems, multidimensionality should be implemented. Multidimensional gradient descent is a more generalized disorder where the input is a vector of the objective function, and the output is a scalar.

For example, consider the input to the objective function 𝑓:𝑅𝑑⟶𝑅
 as a 𝑑-dimensional vector of 𝑥=[𝑥1,𝑥2,…,𝑥𝑑]𝑇. Gradients of the objective function 𝑓(𝑥) with respect to 𝑥
 are vectors (multidimensional gradients) composed of 𝑑
 partial derivatives:

$$\nabla(x)f(x)=[\frac{\partial f(x)}{\partial x_1},\frac{\partial f(x)}{\partial x_2},\cdots,\frac{\partial f(x)}{\partial x_d}]$$

By applying the gradient descent algorithm to the objective function $f(x)$, you can continuously reduce its value:

$$x \leftarrow x-\alpha\nabla f(x)$$