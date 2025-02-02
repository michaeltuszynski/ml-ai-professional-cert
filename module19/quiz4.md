# Module 19 Quiz 4: Matrix Factorization and Collaborative Filtering

## Question 1 (1 point)
Consider the user factors and item factors provided in the tables below.

Q: Z × N | Ommazh | Melt-Banana | BTS | Zhou Shen | Sanam
---|---|---|---|---|---
F1 | −1.53 | −1.77 | 1.16 | 1.09 | 0.73
F2 | 1.77 | 1.88 | 1.45 | 1.74 | 1.69

P: M × Z | F1 | F2
---|---|---
An | −1.52 | 1.35
Bhavana | −1.51 | 1.11
Cordelia | 1.15 | 2.16
Diego | 1.19 | 2.15

Given the user factors and item factors, what would be user "An's" rating for item "Ommazh"?

**Options:**
1. −1.53 × −1.52 + 1.77 × 1.35
2. −1.52 + 1.77 × 1.35
3. −1.53 × 1.35 + 1.77 × −1.52
4. −1.53 × −1.52 + 1.77

**Answer:** Option 1: −1.53 × −1.52 + 1.77 × 1.35
The rating is calculated by taking the dot product of the user's factors and the item's factors. For user An and item Ommazh, we multiply corresponding factors and sum them: (F1_user × F1_item) + (F2_user × F2_item).

---

## Question 2 (1 point)
Given that there are four users and five items, and 50 latent factors are used, what are the dimensions of the user factors matrix P and the item factors matrix Q?

**Options:**
1. User factors matrix P is 4 × 50; item factors matrix Q is 50 × 5
2. User factors matrix P is 50 × 4; item factors matrix Q is 50 × 5
3. User factors matrix P is 4 × 50; item factors matrix Q is 5 × 50
4. User factors matrix P is 4 × 5; item factors matrix Q is 50 × 50

**Answer:** Option 1: User factors matrix P is 4 × 50; item factors matrix Q is 50 × 5
In matrix factorization, P has dimensions (number of users × number of factors) and Q has dimensions (number of factors × number of items). This allows matrix multiplication P × Q to produce the ratings matrix of size (number of users × number of items).

---

## Question 3 (1 point)
Which of the following statements accurately describes the decomposition performed by the Funk SVD algorithm?

**Options:**
1. The Funk SVD algorithm decomposes an M × N matrix into three matrices of sizes M × N, N × F, and F × F
2. The Funk SVD algorithm decomposes an M × N matrix into two matrices of sizes M × N and N × N
3. The Funk SVD algorithm decomposes an M × N matrix into two matrices of sizes M × F and F × N
4. The Funk SVD algorithm decomposes an M × N matrix into three matrices of sizes M × N, M × N, and N × N

**Answer:** Option 3: The Funk SVD algorithm decomposes an M × N matrix into two matrices of sizes M × F and F × N
The Funk SVD algorithm factorizes the ratings matrix (M users × N items) into two matrices: a user factors matrix (M users × F factors) and an item factors matrix (F factors × N items). This decomposition allows for efficient representation of user-item interactions through latent factors.

---

## Answer Key
1. Option 1 (Matrix multiplication dot product calculation for user-item rating)
2. Option 1 (Correct matrix dimensions for collaborative filtering with latent factors)
3. Option 3 (Fundamental matrix decomposition in Funk SVD algorithm)
