# Live Session 2 Summary - Module 12

## Capstone Project Updates & Guidelines

### One-on-One Check-ins
- Students should schedule one-on-one check-ins with learning facilitators
- Purpose: Refine problem statements, identify data sources, and suggest methodologies
- Early check-ins have helped students narrow down general ideas to specific problems with defined datasets

### GitHub Repository Requirements
- README should include:
  - Problem statement
  - Links to code/notebooks
  - Summary of key findings and interpretation
  - Use markdown formatting
- Repository structure:
  - Jupyter notebook files (upload from Google Colab)
  - Data folder for CSV files (25MB size limit)
  - Images folder for visualizations
  - Clear organization and documentation

### Timeline & Milestones
1. Current: One-on-one check-ins
2. Week 16: Formal problem proposal due
3. Week 20: Initial project report due (complete notebook)
4. Weeks 21-23: Second one-on-one with program leader
5. Week 24: Final submission

## K-Nearest Neighbors (KNN) Classification

### Core Concepts
- Classification based on similarity to neighboring data points
- Process:
  1. Define K (number of neighbors)
  2. Calculate distances
  3. Identify K nearest neighbors
  4. Make prediction based on majority class

### When to Use KNN
Ideal conditions:
- Labeled data available
- Multiple instances of each class
- Few features/simple feature space
- Balanced class distribution
- Quick updates needed
- Intuitive explanation required

### Limitations
- Sensitive to irrelevant features
- May struggle with large training datasets
- Less sophisticated than other classification models
- Performance depends heavily on choosing appropriate K value

### Practical Applications
- Converting regression problems to classification:
  - Example: Converting continuous price predictions to price brackets
  - Creating discrete categories from continuous variables
  - Using bucketing functions to transform data

## Key Takeaways
1. Choose appropriate tools based on problem characteristics
2. Ensure data quality and quantity matches model requirements
3. Consider model limitations and alternatives
4. Document work clearly and comprehensively
5. Follow project timelines and milestones