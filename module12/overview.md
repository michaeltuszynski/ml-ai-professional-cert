# Overview: Problem Identification

Before focusing specifically on classification, let us review the different types of problems you have tackled so far and compare them against the classification task.

In Module 1, you explored various types of machine learning algorithms. Now, let us have a brief overview of some other fundamental machine learning algorithms you've learned so far.

## Clustering (Module 6)
Clustering is an unsupervised learning model that groups a population or set of data points in such a way that data points in the same group are similar to each other. In Module 6, you used the k-means algorithm to perform clustering. The goal of k-means is to group data points into k clusters based on similarity or closeness between clusters.

## Regression (Module 7)
Regression is a supervised learning model that predicts the relationship between a dependent variable and one or more independent variables. Regression, at its core, is simply comparing one variable with another variable and finding the relationship between them. Regression also allows you to observe how strongly one variable influences another. Linear regression, specifically, assumes that the relationship between variables can be plotted using a straight line.

## Time Series (Module 10)
Time series can be a supervised or unsupervised learning model that orders a series of data points according to time. This method uses time as an independent variable, and its goal is to make a future forecast. Analysts use time series analysis to record data points at consistent intervals over a set duration that can then be used to model, simulate, and forecast behavior and inform strategic decision-making. Time series has many practical applications in business, economics, and finance, but it can be applied to any industry that compiles consistent historical data for analysis.

This module includes classification.

## Classification (Module 12)
Classification is a supervised learning model that involves predicting the value of a target variable by constructing a model based on one or more predictor variables. The predicted output can either be a discrete output class or a continuous-valued variable. When the output represents a category or class, it falls under supervised classification. On the other hand, if the output predicts continuous values (such as house prices in a housing prediction model), it is regression. In Module 7, you delved extensively into linear regression. Now, in this module, you will explore how machine learning models assist in predicting categorical outputs.

Examine the table below to learn how classification compares to the other methods mentioned in this overview.

### Classification Comparison

| Aspect | Classification | Clustering | Regression | Time Series |
|--------|---------------|------------|------------|-------------|
| **Definition** | Predicts the value of a target variable by building a model based on one or more predictors | Groups a population or set of data points | Predicts the relationship between the dependent variable and one or more independent variables | Uses time as an independent variable whose goal is to make a future forecast |
| **Goal** | To compute the category of data | To group similar items into clusters | To forecast or predict | To provide a future forecast |
| **Real-World Applications** | Email spam protection, customer churn, conversion prediction | Fraud detection, similarity pattern detection, genetics | Stock market price predictions, insights on customer behavior, marketing effectiveness | Seasonality, weather forecast, financial market trend analysis |
| **Algorithm** | K-nearest neighbors, decision trees | K-means | Linear regression | AutoRegressive Moving Average (ARMA) |
