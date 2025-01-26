# Mini-Lesson 18.5: Bag-of-Words and TF–IDF

## Bag-of-Words

**Description**: It represents text as a vector of word counts or frequencies.

### Process:
1. Create a vocabulary of all unique words in the corpus.
2. Each document is converted into a vector, where each dimension corresponds to a word in the vocabulary.
3. The value of each dimension is the count or frequency of the corresponding word in the document.

### Examples of Bag-of-words (BoW)

#### Example 1: Sentence: "Cats are friendly animals."

**Steps to Compute BoW:**

1. **Tokenize the sentence:**
   - Tokens: `["Cats", "are", "friendly", "animals"]`

2. **Create the vocabulary:**
   - Vocabulary: `["Cats", "are", "friendly", "animals"]`

3. **Compute the BoW vector:**
   Count of each word in the sentence:
   - "Cats": 1
   - "are": 1
   - "friendly": 1
   - "animals": 1

   BoW Vector: `[1, 1, 1, 1]`

   BoW Vector Representation: `[1, 1, 1, 1]` where each value corresponds to the count of each word in the vocabulary.

#### Example 2: Sentence: "Dogs are friendly animals. Friendly dogs are loyal."

**Steps to Compute BoW:**

1. **Tokenize the sentence:**
   - Tokens: `["Dogs", "are", "friendly", "animals", "Friendly", "dogs", "are", "loyal"]`

2. **Create the vocabulary:**
   - Vocabulary: `["Dogs", "are", "friendly", "animals", "loyal"]`

3. **Compute the BoW vector:**
   Count of each word in the sentence:
   - "Dogs": 2
   - "are": 2
   - "friendly": 2
   - "animals": 1
   - "loyal": 1

   BoW Vector: `[2, 2, 2, 1, 1]`

   BoW vector representation: `[2, 2, 2, 1, 1]` where each value corresponds to the count of each word in the vocabulary.

## TF-IDF

TF–IDF stands for term frequency–inverse document frequency. It is a numerical statistic used in text processing and information retrieval to reflect the importance of a word in a document relative to a collection of documents or corpus. It helps in evaluating how significant a word is in a specific document compared to its frequency across all documents.

### Components of TF–IDF:

#### Term Frequency (TF):
- **Definition**: It measures how frequently a term occurs in a document.
- **Formula**: TF(t,d)
- **Example**: If the term "apple" appears three times in a document with 100 words, then:
  ```
  TF("apple", d) = 0.03
  ```

#### Inverse Document Frequency (IDF)
- **Definition**: Measures the importance of the term in the entire corpus. Words that appear in many documents are less significant.

The general formula for inverse document frequency (IDF) is given by:

```
IDF(t,D) = log((N+1)/(1+DF(t,D))) + 1
```

Where:
- t = Term of interest
- D = Set of all documents (corpus)
- N = Total number of documents in the corpus
- DF(t,D) = Number of documents in the corpus containing the term t

The addition of 1 to both the numerator and denominator is used to prevent issues with terms that appear in every document. It avoids division by zero and ensures that terms with very high document frequencies do not lead to an IDF score of 0 or negative values.

**Example**: If "apple" appears in ten out of 1,000 documents:
```
IDF("apple", D) = log((1000+1)/(10+1)) + 1 = 3 (approximately)
```

#### TF–IDF Score:
- **Definition**: It combines TF and IDF to compute a term's overall importance in a document.
- **Formula**: `TF-IDF(t,d,D) = TF(t,d) × IDF(t,D)`
- **Example**: Continuing from above, if TF for "apple" is 0.03 and IDF is 2:
  ```
  TF-IDF("apple",d,D) = 0.03 × 2 = 0.06
  ```

### Advantages, Limitations, and Applications of TF-IDF

| Advantages | Limitations | Applications |
|------------|-------------|--------------|
| Context Sensitivity: It weighs terms by their importance in the document relative to the corpus, capturing the relevance of a term in a specific context. | Simplicity: It does not capture semantic meaning or context beyond word frequency. | Information Retrieval: Enhancing search engine results by ranking documents based on term relevance. |
| Feature Selection: It helps in selecting the most relevant terms for document classification, clustering, and search. | High Dimensionality: It results in a large feature space, especially with large vocabularies. | Text Classification: Feature extraction for ML models. |
| | Static: The model does not adapt to the evolving meaning of terms over time. | Clustering: Identifying and grouping similar documents based on term significance |