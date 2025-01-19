# Mini-Lesson 12.2: Calculating K-Nearest Neighbors

## K-Nearest Neighbors

**Definition:** KNN is a supervised learning algorithm that predicts the class (for classification) or value (for regression) of a new data point based on the similarity to its k nearest neighbors in the training dataset.

### Proximity-Based Prediction:
The objective is to assign the data point to a class (classification) or predict its value (regression) by considering its proximity to existing data points.

KNN does not assume any specific underlying data distribution.

### Phases:
1. **Training Phase:** Data preprocessing occurs. Features and corresponding class labels are organized (in the case of classification).
2. **Prediction Phase:** Given an unlabeled data point (testing data), you can:
   - Calculate the distance (e.g., Euclidean distance) between the testing data point and all training data points.
   - Select the k-nearest neighbors (based on the smallest distances).
   - Assign the majority class among the k neighbors to the testing data point.

Next, let us see a simple example about k-nearest neighbors.

### Consider the following dataset:
A dataset including four columns: Name, Age, Gender, and Class of Sports

| Name    | Age | Gender | Class of Sports |
|---------|-----|--------|----------------|
| Ajay    | 32  | 0      | Football       |
| Mark    | 40  | 0      | Neither        |
| Sara    | 16  | 1      | Cricket        |
| Zaira   | 34  | 1      | Cricket        |
| Sachin  | 55  | 0      | Neither        |
| Rahul   | 40  | 0      | Cricket        |
| Pooja   | 20  | 1      | Neither        |
| Smith   | 15  | 0      | Cricket        |
| Laxmi   | 55  | 1      | Football       |
| Michael | 15  | 0      | Football       |

Now, you want to predict the class of sports for a new individual named Angelina.

Angelina's age is five, and her gender is female (1).

**NOTE:** Male is denoted with numeric value 0, and female is denoted with 1.

You will use the Euclidean distance formula to find the distance between Angelina and each existing data point.

- Distance between Angelina and Ajay: D = ((5 − 32)² + (1 − 0))½ = 27.02
- Distance between Angelina and Mark: 35.01
- Distance between Angelina and Sara: 11.0
- Distance between Angelina and Zaira: 29.0
- Distance between Angelina and Sachin: 50.01
- Distance between Angelina and Rahul: 35.01
- Distance between Angelina and Pooja: 15.0
- Distance between Angelina and Smith: 10.05
- Distance between Angelina and Laxmi: 50.0
- Distance between Angelina and Michael: 10.05

The three closest distances are 10.05, 10.05, and 11 (corresponding to Smith, Michael, and Sara). Since both Smith and Michael play cricket, as per voting, Angelina should play cricket as well. The parameter k determines how many neighbors to consider during the prediction.