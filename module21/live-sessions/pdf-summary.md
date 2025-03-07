## Summary of Deep Neural Networks Module 21 - Part 1


This document summarizes the key topics covered in the first part of the Deep Neural Networks module, based on the Office Hours session led by Francesca Vera on February 24, 2025 [1].


### Capstone Administration & Feedback [2-4]


*   **Initial reports are due**, and feedback should be reviewed [2].

*   **Schedule 1:1 meetings with your LF** to discuss questions and feedback [2].

*   **Adjust your project** based on feedback, including more experiments, cleaning up, and writing the report [2].

*   **Clean up your repository!** Use descriptive filenames for notebooks (e.g., `loan_default_predictor.ipynb` instead of `colabnotebook.ipynb` or `project.ipynb`) and organize images in a folder [3].

*   **Utilize formatting features** to clearly present model features (e.g., "Model Features: - Age - Zip Code - Income - Number of Previous Defaults - Loan Amount") [3].

*   **Don't assume prior knowledge** in your repository. Ensure your research question, prediction goals, methodology, justifications for choices (model, feature selection, evaluation metric), and results are clear and concise [3, 4].

*   **Present results in a helpful format**, comparing model performance metrics clearly (e.g., using a table to show train and test accuracy for different models like Random Forest, KNN, and Logistic Regression) [4].


### Concepts in Neural Networks [1, 4-7]


*   The session aims to provide helpful tips and an overview of the module content for individual deeper exploration [1, 4].

*   Simple algorithms like Logistic Regression, SVM, KNN, and Decision Trees can be used for tasks like predicting if a patient has diabetes based on features like glucose concentration, blood pressure, skin thickness, and age [5].

*   However, **for more complicated problems**, especially in computer vision or with language, **more powerful models like Neural Networks are used** [5, 6].

*   Simple classification algorithms might not work well for complex tasks due to complex data, a large number of features, and patterns distributed in ways these algorithms cannot capture [6].

*   **Neural networks use specific feature functions called activation functions** (e.g., Sigmoid, Tanh, ReLU) [6, 7].

*   **Neural networks add coefficients (weights) to all connections in their structure** [6, 7].

*   **Neural networks allow for multiple layers**, which distinguishes them from simpler models [7].


### Neural Network Structure [7, 8]


*   A **neuron** is a fundamental building block of a neural network [7].

*   Understanding a neuron involves considering **inputs** (e.g., Hungry, Yummy, Nut Allergy in the sandwich example), associated **weights**, a **bias term**, and an **activation function** (e.g., ReLU) [7, 8].

*   **Adjustments ("design choices")** can be made to the neural network structure [8].

*   **"Deep" Learning refers to neural networks with more layers** [8].

*   Neural Networks support **multiclass classification** [8].


### Neural Network Training [8, 9]


*   **Loss** can be thought of as the "error" of the network's predictions [8].

*   The goal of training is to **have as low a loss (low "error") as possible** [8].

*   Different networks can have varying loss values for the same prediction task (e.g., classifying an image as Cat or Dog), indicating different levels of accuracy [9]. Network 2 with outputs 0.85 (Cat) and 0.15 (Dog) has a lower loss than Network 1 (0.6 Cat, 0.4 Dog) and Network 3 (0.1 Cat, 0.9 Dog) when the true label is Cat [9].


### What to expect in Part 2 [1, 4]


*   Part 2 of the module will likely delve deeper into the concepts of neural networks, potentially including topics beyond the introductory overview provided in this session [1, 4].

*   An example walkthrough will be provided during the Office Hours [1, 4].