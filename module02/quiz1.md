# Probability and Uniform Distributions Quiz

## Question 1 (1 point)
What is the probability of rolling a 4 on a six-sided die?

**Options:**
1. 1/4
2. 1
3. 1/5
4. 1/6

**Answer:** Option 4: 1/6
- Core definition: In a fair six-sided die, each number has an equal probability of 1/6
- This follows from the basic principle of probability where P(event) = favorable outcomes / total outcomes
- For a single number on a fair die: 1 favorable outcome / 6 possible outcomes = 1/6

---

## Question 2 (1 point)
What is the formula for the expected value E[X] for discrete and continuous uniform distributions?

**Options:**
1. (a + b) / 2
2. a + b
3. (a × b) / 2
4. (a − b) / 2

**Answer:** Option 1: (a + b) / 2
- Core definition: The expected value of a uniform distribution is the arithmetic mean of its endpoints
- For both discrete and continuous uniform distributions on interval [a,b], E[X] = (a + b) / 2
- This represents the center point or average value of the distribution

---

## Question 3 (1 point)
If a continuous random variable 𝑋 is uniformly distributed between 2 and 8, what is the variance of X?

**Options:**
1. 3
2. 4
3. 6
4. 9

**Answer:** Option 4: 9
- Core definition: For a continuous uniform distribution on interval [a,b], the variance is (b-a)²/12
- Calculation: For X ~ U(2,8): (8-2)²/12 = 36/4 = 9
- This measures the spread of values around the mean, with larger values indicating greater dispersion

---

## Question 4 (1 point)
A uniform distribution ranging from a to b is made using this Python statement:
`U = uniform(loc,scale)`.

What does the constructor `loc` represent?

**Options:**
1. loc = a
2. loc = a − b
3. loc = b − a
4. loc = b

**Answer:** Option 1: loc = a
- Core definition: In scipy/numpy's uniform distribution, `loc` parameter represents the lower bound (a)
- Implementation detail: The `scale` parameter represents the range (b-a)
- Together they define the interval [loc, loc+scale] for the distribution

---

## Question 5 (1 point)
If a uniform distribution is formulated in Python as `U = uniform(loc=10, scale=5)`, what is the output of the statement `U.mean()`?

**Options:**
1. 10
2. 5
3. 12.5
4. 12

**Answer:** Option 3: 12.5
- Core definition: Mean = loc + scale/2
- Calculation: 10 + 5/2 = 12.5
- This follows from the general formula (a + b)/2 where a=loc and b=loc+scale

---

## Answer Key
1. Option 4: 1/6 (Equal probability for each face of a fair die)
2. Option 1: (a + b) / 2 (Arithmetic mean of endpoints)
3. Option 4: 9 (Variance formula: (b-a)²/12 = 36/4 = 9)
4. Option 1: loc = a (Lower bound of uniform distribution)
5. Option 3: 12.5 (Mean formula: loc + scale/2)