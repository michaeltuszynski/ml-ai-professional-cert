# Mini-Lesson 3.1: The CRISP-DM Framework

As has been previously mentioned, CRISP-DM is an industry-proven way to guide successful data science efforts. The framework includes the following phases: business understanding, data understanding, data preparation, modeling, evaluation, and deployment. Learn more about each phase of the process and the associated tasks below.

## Business Understanding

### Determine the Business Objectives
- **Background**
- **Business Objectives**
- **Business Success Criteria**

### Assess the Situation
- **Inventory of Resources Requirements, Assumptions, and Constraints**
- **Risks and Contingencies**
- **Terminology**
- **Cost and Benefits**

### Determine the Data-Mining Goals
- **Data-Mining Goals**
- **Data-Mining Success Criteria**

### Produce the Project Plan
- **Project Plan**
- **Initial Assessment of Tools and Techniques**

## Data Understanding
### Collect the Initial Data
- **Initial Data Collection Report**

### Describe the Data
- **Data Description Report**

### Explore the Data
- **Data Exploration Report**

### Verify the Data Quality
- **Data Quality Report**

## Data Preparation
### Select the Data
- **Rationale for Inclusion/Exclusion**

### Clean the Data
- **Data Cleaning Report**

### Construct the Data
- **Derived Attributes**
- **Generated Records**

### Integrate the Data
- **Merged Data**

### Format the Data
- **Reformatted Data**

## Modeling
### Select the Modeling Technique
- **Modeling Techniques**
- **Modeling Assumptions**

### Generate the Test Design
- **Test Design**

### Build the Model
- **Parameter Setting**
- **Models**
- **Model Description**

### Assess the Model
- **Model Assessment**
- **Revised Parameter Setting**

## Evaluation
### Evaluate the Results
- **Assessment of Data-Mining Results with Respect to Business Success Criteria**
- **Approved Models**

### Review the Process
- **Process Review**

### Determine the Next Steps
- **List of Possible Actions**
- **Decision**

## Deployment
### Plan the Deployment
- **Deployment Plan**

### Plan the Monitoring and Maintenance
- **Monitoring and Maintenance Plan**

### Produce the Final Report
- **Final Report**
- **Final Presentation**

### Review the Project
- **Experience Documentation**

## Example Application: House Price Prediction

### Business Understanding
As mentioned above, CRISP-DM starts with understanding a business problem. One such example of a business problem could be estimating the sale prices of houses. Imagine the client in this example is interested in predicting house prices based on a couple of features of the house—namely, square footage and the year the house was built. To be more precise, you could boil this project down to the following three business questions:

1. What is the square footage of the house?
2. What year was the house built?
3. Can the price of a house be predicted based on these two features with reasonable accuracy?

### Data Understanding and Preparation
In this phase, you need to understand and prepare your data. Suppose you have the following data to work with:

| Price        | Square Footage | Bedrooms | Bathrooms | Stories | Guest Room | Basement | Hot Water | Air Conditioning | Parking | Preferred Area | ZIP Code |
|-------------:|--------------:|:--------:|:---------:|:-------:|:----------:|:--------:|:---------:|:---------------:|:--------:|:-------------:|:--------:|
| ?            | 7,420         | 4        | 2         | 3       | No         | No       | No        | Yes             | 2        | Yes           | 90210    |
| 12,250,000   | 8,960         | 4        | 4         | 4       | No         | No       | No        | Yes             | 3        | No            | 90094    |
| ?            | 9,960         | 3        | 2         | 2       | No         | NaN      | No        | No              | 2        | Yes           | 90077    |
| 12,250,000   | 7,500         | 4        | 2         | 2       | No         | Yes      | No        | Yes             | NaN      | Yes           | 90245    |
| 11,410,000   | 7,420         | 4        | 1         | 2       | Yes        | Yes      | No        | Yes             | 2        | NaN           | 90003    |
| ?            | 7,500         | 3        | 3         | 1       | No         | Yes      | NaN       | Yes             | 2        | Yes           | 90002    |
| 10,150,000   | 8,580         | 4        | 3         | 4       | No         | No       | No        | Yes             | NaN      | Yes           | 90001    |
| 10,150,000   | 16,200        | 5        | 3         | 2       | No         | No       | No        | No              | 0        | No            | 90001    |

It is important to remember that the data you have may not contain all of the information needed to predict prices accurately. Historically, features such as 'bedrooms' and 'bathrooms' have been a predictor of price, but in this case, the client wants to predict house prices based on square footage and/or the year a house was built. Since this data does not include the year each house was built, you should first make predictions based on the square footage. The far-left column is the predicted price based on this feature. The data contains missing values such as "NaN," which signals to you that data cleaning is necessary.

### Modeling
Next, you have to choose a model for your data. In this case, a linear regression model can predict house prices based on the features outlined in the dataset. The following is an example: Given the square foot (𝑓𝑡²) of a house for which the price is unknown, regression will analyze the linear relationship between price and square footage to make the prediction. Therefore, the linear equation for predicting house prices based on square footage might look something like the following:

```
price = 𝑘₀ + 𝑘₁𝑓𝑡²
```

### Evaluation
Finally, you have to evaluate the performance of the linear regression model. Root mean squared error (RMSE) is the most commonly used measure to assess regression models. It is the average of the squared difference between each predicted price and the actual price.

## Why Is CRISP-DM Important to a Data Scientist?

Among a variety of other reasons, the CRISP-DM framework is important to data scientists because it:

1. Includes several processes that take care of simple data-mining tasks
2. Promotes best practices and facilitates the replication of projects
3. Provides a uniform framework for planning and managing projects
4. Is a cross-industry standard to be used by any data science project, regardless of its domain