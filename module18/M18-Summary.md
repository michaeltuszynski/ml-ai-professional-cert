# Module 18: Natural Language Processing (NLP) - Video Summaries

## Video 1: Introduction to NLP

### Main Topic and Key Concepts
- Natural Language Processing (NLP): Making human language accessible to computers
- Key challenges in processing language vs. numbers:
  - Word order affects meaning
  - Context-dependent word meanings
  - Human communication imprecision
  - Individual communication styles

### Real-World Applications
1. Internet search engines (Google Search)
2. Spam filtering
3. Machine translation
4. Dialogue systems and chatbots
5. Text summarization
6. Text categorization
7. Sentiment analysis
8. Speech recognition (Alexa, Siri, Google Assistant)

### ML Workflow Comparison
#### Standard ML Workflow
1. Data splitting (train/test)
2. Preprocessing
   - Handle missing values
   - Remove useless columns
   - Normalize data
3. Feature building
4. Model training
5. Validation
6. Testing

#### NLP-Specific Workflow
1. Corpus splitting (train/test)
   - Corpus: Large body of text
   - Document: Individual text sample
2. Preprocessing
   - Text tokenization
   - Text normalization
3. Feature extraction
   - Bag-of-words
   - TF-IDF
4. Model training
5. Validation
6. Testing

### Tools and Technologies
- Primary tool: Natural Language Toolkit (NLTK)
- Similar to scikit-learn in accessibility

## Video 2: NLTK Tokenization

### Main Topic and Key Concepts
- Tokenization: Breaking text into individual units
- Types of tokenization:
  - Sentence tokenization
  - Word tokenization

### Technical Implementation
```python
# Example using NLTK
import nltk
nltk.download()  # Downloads manager for datasets
nltk.download('twitter_samples')  # Specific dataset download
```

### Practical Examples
- Movie review tokenization example:
  - Input: "I enjoyed 'Minority Report.' Tom Cruise didn't disappoint..."
  - Output: 36 tokenized words including punctuation

### Key Takeaways
- Tokenization is language-specific
- English is relatively easy (space-based splitting)
- Other languages (German, Chinese) require more complex rules
- Different tokenizers have different rule sets

## Video 3: Text Normalization

### Main Topic and Key Concepts
- Text normalization: Operations that transform tokens while preserving their format
- Different from feature extraction which converts tokens to numbers

### Normalization Operations
1. Case conversion
2. Spelling correction
3. Special character removal
4. Stop word removal
5. Parts of speech tagging
6. Named entity recognition
7. Stemming
8. Lemmatization

### Technical Details
#### Parts of Speech Tagging
```python
from nltk import pos_tag
# Example tags: NNP (proper noun), PRP$ (possessive pronoun)
```

#### Named Entity Recognition
- Types: Organization, Person, Location, Date, Time
```python
from nltk import ne_chunk
```

#### Stemming vs Lemmatization
- Stemming (Porter Stemmer)
  - Rule-based
  - Can produce non-words
  - Example: "joyous" → "joy-o-u"

- Lemmatization (WordNet)
  - Produces only real words
  - More language knowledge required
  - Example: "geese" → "goose"

### Best Practices
- Choose normalization operations based on task requirements
- Consider trade-offs between text coherence and feature reduction
- Use stemming for sentiment analysis
- Use lemmatization when grammatical coherence matters

## Video 4: Bag-of-Words and TF-IDF

### Main Topic and Key Concepts
- Feature extraction methods for converting tokens to numerical format
- Progression: Bag-of-Words → TF-IDF → Word Vectorization

### Bag-of-Words (BoW)
- Creates feature for each unique token
- Counts token occurrences in each document
- Limitations:
  - Loses word order
  - No distinction between informative/uninformative words

### TF-IDF (Term Frequency-Inverse Document Frequency)
- Formula: TF-IDF = TF × IDF
- Term Frequency (TF)
  - Normalized word count in document
  - TF = (word count) / (total words in document)
- Inverse Document Frequency (IDF)
  - Importance measure across documents
  - IDF = -log(documents containing term / total documents)

### Best Practices
- Choose method based on:
  - Application requirements
  - Data volume
  - Model performance needs

## Video 5: Naive Bayes

### Main Topic and Key Concepts
- Naive Bayes classifier for text classification
- Comparison with logistic regression
- Based on Bayes' rule and feature independence assumption

### Technical Details
#### Model Components
1. Probability estimation
   - P(class|features) ∝ P(features|class) × P(class)
2. Independence assumption
   - Features are conditionally independent given class
3. Parameter estimation
   - Based on counting occurrences
4. Laplace smoothing
   - Handles zero probabilities

### Mathematical Foundation
```
h(x) = argmax_κ[P(x|κ)P(κ)]
P(x|κ) = ∏P(x_i|κ)  # Due to independence assumption
```

### Advantages
- Simple linear model
- Few parameters
- Efficient for high-dimensional problems
- Works well with text classification

## Video 6: Training and Evaluation

### Main Topic and Key Concepts
- Practical implementation of sentiment analysis for Twitter data
- Comparison of Naive Bayes and Logistic Regression

### Implementation Steps
1. Data preparation
```python
import nltk
nltk.download('twitter_samples')
# 10,000 tweets (5,000 positive, 5,000 negative)
```

2. Preprocessing
   - Custom tweet tokenization
   - Stop word removal
   - Porter Stemming

3. Feature extraction
   - Bag-of-words implementation
   - Sparse matrix handling

4. Model training and evaluation
   - Naive Bayes implementation
   - Logistic Regression comparison

### Results and Insights
- Both models achieved ~99.8% accuracy
- Emoticons were strongest predictors
- Reduced feature set (emoticons only) improved performance
- Sparse matrix characteristics:
  - 10,225 features
  - 0.08% non-zero entries

### Best Practices
- Collect preprocessing steps in single function
- Handle sparse matrices efficiently
- Consider feature importance in model evaluation
- Test with reduced feature sets for efficiency

### Future Directions
- Excluding emoticons analysis
- TF-IDF implementation
- Other classifier comparisons (SVM, Decision Trees)
- Advanced NLP topics:
  - Machine translation
  - Text generation
  - Conversational AI