# Natural Language Processing Quiz 4

## Question 1 (1 point)
In the bag-of-words feature extraction technique, if there are five unique tokens in the data containing ten documents, how many features would there be in the feature matrix?

**Options:**
1. 15
2. Five
3. 50
4. Ten

**Answer:** Option 2: Five
- Core definition: In bag-of-words, the number of features equals the number of unique tokens in the vocabulary
- Explanation: Each unique token becomes one feature, regardless of the number of documents
- Implementation detail: The feature matrix will have dimensions of (10 documents × 5 features), but the number of features is just the vocabulary size

---

## Question 2 (1 point)
Which of the following statements is true regarding the bag-of-words (BoW) model?

**Options:**
1. Bag-of-words represents each document as a vector of unique tokens
2. Bag-of-words does not keep track of informative words
3. Bag-of-words does not keep track of the frequency of words in a document
4. Bag-of-words keeps track of the order of words in a document

**Answer:** Option 1: Bag-of-words represents each document as a vector of unique tokens
- Core definition: BoW converts text into fixed-length vectors based on vocabulary
- Implementation detail: Each document becomes a vector where each position represents a token's frequency
- Note: BoW specifically does track word frequencies but ignores word order

---

## Question 3 (1 point)
What is the correct representation of the TF–IDF equation?

**Options:**
1. tf(t,d) / idf(t)
2. tf(t,d) × idf(t)
3. tf(t,d) − idf(t)
4. tf(t,d) + idf(t)

**Answer:** Option 2: tf(t,d) × idf(t)
- Core definition: TF-IDF combines term frequency (TF) and inverse document frequency (IDF) through multiplication
- Implementation detail: This multiplication balances local term importance (TF) with global term uniqueness (IDF)

---

## Question 4 (1 point)
Consider a document containing tokens: {'enjoy','disappoint','great','bore','bore'}. What would the TF score for the feature "bore" be?

**Options:**
1. 0.4
2. 0.25
3. 0
4. 0.75

**Answer:** Option 1: 0.4
- Core definition: Term Frequency (TF) = (Number of times term appears) / (Total number of terms)
- Calculation: 2 occurrences of "bore" / 5 total terms = 0.4
- Implementation detail: Raw frequency is normalized by document length

---

## Answer Key
1. Option 2: Five (Number of features equals vocabulary size)
2. Option 1: Bag-of-words represents each document as a vector of unique tokens (Core BoW representation)
3. Option 2: tf(t,d) × idf(t) (Standard TF-IDF formula)
4. Option 1: 0.4 (TF calculation: 2/5 = 0.4)