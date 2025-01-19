## Module 13 - Live Session 1 Summary: Introduction to Logistic Regression

### Administrative Updates
- Module 11 practical application assignments have been graded
- Students showed improvement from Module 5 practical applications
- Reminder to book one-on-one capstone project consultations before holiday break
- Consultations should be booked with assigned learning facilitators
- Students should come prepared with project ideas as facilitators cannot suggest topics

### Main Topic: Logistic Regression

#### Key Concepts
- Logistic regression is a classification algorithm despite its name
- Uses logistic/sigmoid function which maps any input to values between 0 and 1
- Output can be interpreted as probability of belonging to a class
- Similar mathematical foundations to linear regression but used for classification

#### Case Study: Titanic Dataset Analysis

##### Data Cleaning Steps:
1. Handling Missing Values:
   - Age (20% missing): Filled with median due to skewed distribution
   - Cabin (77% missing): Dropped due to high missing percentage and low relevance
   - Embarked (0.22% missing): Filled with most common value (Southampton)

2. Feature Engineering:
   - Combined SibSp and Parch into "Travel_alone" column
   - Created "is_minor" column based on age < 17
   - Applied get_dummies to P_class, sex, and embarked columns
   - Removed redundant columns (PassengerId, name, ticket)

3. Feature Selection:
   - Used Recursive Feature Elimination (RFE)
   - Selected top 4 features: P_class_1, P_class_2, sex_male, is_minor
   - Verified low correlation between selected features using heatmap

#### Model Results
- Achieved 77% accuracy as baseline model
- Low error rate indicating good model performance
- Demonstrates logistic regression's effectiveness as baseline classifier

### Best Practices Highlighted
- Use median for filling missing values in skewed distributions
- Consider domain knowledge when feature engineering
- Check feature correlations to avoid multicollinearity
- Start with simpler models as baselines
- Use RFE for feature selection in supervised learning
- Choose project topics you're knowledgeable about

### Next Steps
- Students encouraged to experiment with:
  - Different numbers of features in RFE
  - Additional feature engineering
  - Model improvements through grid search and pipelines
- Book capstone consultations for project guidance