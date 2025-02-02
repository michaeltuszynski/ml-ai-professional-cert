# Module 19 Quiz 1: Recommendation Systems

## Question 1 (1 point)
In a recommendation system, what do "item factors" refer to?

**Options:**
1. Factors that describe each item
2. Factors related to the user's demographic information
3. Factors that indicate the user's interaction history with other users
4. Factors related to the system's computational resources

**Answer:** Option 1: Factors that describe each item

Item factors are the specific features or characteristics that define and describe each item in a recommendation system. These factors form the basis for understanding item similarities and making content-based recommendations.

---

## Question 2 (1 point)
Imagine that you are using the item factors "lo-fi_indie" and "slick_pop" and the user rating to build a linear regression model. The parameters that you get from linear regression are θ₁ and θ₂. In the context of the recommendation system, what are these parameters known as?

**Options:**
1. Intercepts
2. Linear factors
3. User factors
4. Item factors

**Answer:** Option 3: User factors

These parameters (θ₁ and θ₂) represent user factors because they indicate how much weight a user gives to each item factor dimension (in this case, lo-fi_indie and slick_pop). They capture the user's preferences in terms of these musical style dimensions.

---

## Question 3 (1 point)
In a recommendation system, how are predictions made when applying linear regression to item factors and ratings data?

**Options:**
1. By combining the ratings given by similar users using a weighted sum
2. By calculating the dot product of user and item latent factors
3. By averaging the historical ratings of all items for each user
4. By summing the weighted item features and user features, plus an intercept term

**Answer:** Option 4: By summing the weighted item features and user features, plus an intercept term

In linear regression-based recommendation systems, predictions are made by combining item features and user features through weighted sums (with weights learned during training) and adding an intercept term to account for base rating levels.

---

## Question 4 (1 point)
What is a major issue with content-based filtering in real-world scenarios?

**Options:**
1. It requires extensive user interaction data to be effective
2. It relies too heavily on collaborative filtering methods
3. Items are not typically categorized into content categories
4. It often fails to account for user demographic information

**Answer:** Option 3: Items are not typically categorized into content categories

The primary challenge with content-based filtering is that many items lack proper content categorization or feature descriptions, making it difficult to compute meaningful item similarities and recommendations based on content alone.

---

## Answer Key

1. Option 1: Factors that describe each item (Core definition of item factors in recommendation systems)
2. Option 3: User factors (Parameters representing user preferences for each item factor dimension)
3. Option 4: By summing weighted features plus intercept (Mathematical basis of linear regression in recommendations)
4. Option 3: Items not typically categorized (Key practical limitation of content-based filtering)
