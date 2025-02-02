# Required Discussion 19:1: Building a Recommendation System with SURPRISE

## Learning Outcome Addressed
- Use the SURPRISE library to build and analyze recommender systems on real datasets.

This is a required discussion and counts toward program completion.

This activity focuses on exploring additional algorithms with the SURPRISE library to generate recommendations. Using the provided [Jupyter Notebook](module19/discussion.md module19/discussion19_1.ipynb), identify the optimal algorithm by minimizing the mean squared error (MSE) using cross-validation. You are also going to select a dataset to use from the [grouplens](https://grouplens.org) example datasets.

We are using the data in 'data/ml100k' -  the MovieLens 100K dataset for working with SURPRISE. Here's why:

It's a stable benchmark dataset with a manageable size
It contains exactly what we need for SURPRISE:

Users: 1000 users
Items: 1700 movies
Ratings: 100,000 ratings

The dataset is well-documented and in a clean format
It's small enough to work with easily but large enough to be meaningful
It's specifically designed as a benchmark dataset, so it's well-suited for testing recommendation algorithms

The data in MovieLens 100K is structured in a way that's compatible with SURPRISE's expected format, with user IDs, movie IDs, and ratings. The ratings are on a 1-5 scale, which is perfect for recommendation system development.

Then, compare the performance of at least the KNNBasic, SVD, NMF, SlopeOne, and CoClustering algorithms to build your recommendations. For more information on the algorithms, check out this [documentation for the algorithm package](https://surprise.readthedocs.io/en/stable/prediction_algorithms_package.html).

This is a required try-it activity and counts toward program completion.

## Submission Instructions:
1. Share the results of your investigation and include the results of your cross-validation and a basic description of your dataset with your peers.
2. Once you have submitted your post, read the statements posted by your peers, and respond to at least two of them.

Your initial post should be no more than 200 words. Your responses to others' posts should be no more than 150 words.