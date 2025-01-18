## Dataset Analysis: Global Mortality Rates (1950-2023)

I analyzed a dataset tracking mortality rates across major world regions (Africa, Americas, Asia, and Europe) spanning from 1950 to 2023. This analysis focused on understanding temporal patterns in global mortality rates.

### Cross-Validation Methods Comparison

I evaluated two distinct cross-validation approaches:

1. **Traditional K-Fold Cross-Validation**
   - Randomly splits data into 5 parts
   - Mixes temporal information randomly

2. **Time Series Split Cross-Validation**
   - Splits data chronologically
   - Uses earlier years to predict later periods

### Results and Justification

Time Series Split proved to be the superior approach for this analysis for several key reasons:

1. **Data Temporal Nature**
   - The data is inherently time-based (yearly mortality rates)
   - More logical to use historical data to predict future trends

2. **Real-World Applicability**
   - Better reflects actual forecasting scenarios
   - Cannot use future information to predict past events

3. **Model Reliability**
   - Provides more realistic performance metrics
   - Aligns with practical implementation scenarios

### Conclusion

While traditional K-Fold cross-validation showed numerically better performance metrics, these results were likely optimistically biased due to the random mixing of temporal data. The Time Series Split approach provides a more realistic assessment of the model's predictive capabilities in real-world applications.