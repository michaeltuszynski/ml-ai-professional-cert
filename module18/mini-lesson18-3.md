# Mini-Lesson 18.3: NLTK and Tokenization

Tokenization is the process of breaking down a stream of text into smaller units, which are called tokens. These tokens can be words, phrases, symbols, or other meaningful elements depending on the context and the task at hand in NLP.

## Purpose of Tokenization in NLP
- Text Preprocessing: Before any further analysis or modeling, text data often needs to be divided into smaller units that can be processed more easily.
- Feature Extraction: Tokens serve as the basic building blocks for various NLP tasks, such as text classification, named entity recognition, sentiment analysis, and machine translation.
- Text Representation: Tokens are essential for creating numerical representations of text data, such as through vectorization or word embeddings.

## Types of Tokenization

### 1. Word Tokenization
This is the most common form, where text is split into words based on whitespace and punctuation.

**Example Text:**
```
"Tokenization is a crucial step in natural language processing (NLP). It involves breaking down text into smaller units, such as words or phrases, for analysis."
```

**Word Tokens:**
```
Tokenization
is
a
crucial
step
In
natural
language
processing
(NLP)
.
It
involves
breaking
down
text
into
smaller
units
,
such
as
words
or
phrases
,
for
analysis
.
```

In this example, word tokenization splits the text into individual words, respecting punctuation marks and retaining the structure of the text. Each word becomes a token that can be further analyzed or processed for tasks such as sentiment analysis, named entity recognition, or text classification.

### 2. Sentence Tokenization
In this type of tokenization, text is split into sentences based on punctuation marks such as periods, exclamation marks, and question marks.

**Example Text:**
```
"Tokenization is the first step. It breaks down text into sentences. Each sentence is then processed separately."
```

**Sentence Tokens:**
```
1. Tokenization is the first step.
2. It breaks down text into sentences.
3. Each sentence is then processed separately.
```

Sentence tokenization divides the text into separate sentences based on punctuation marks such as periods, exclamation marks, or question marks. Each sentence token allows for focused analysis or processing of individual sentences, which is essential for tasks such as machine translation, text summarization, or dialogue generation.

### 3. Subword Tokenization
This splits words into smaller units, which is often useful for languages with complex word formations or for generating more robust word representations.

**Example Text:**
```
"Unsupervised learning is a technique used in machine learning."
```

**Subword Tokens:**
```
Un
supervised
learning
is
a
technique
used
in
machine
learning
.
```

Subword tokenization breaks words into smaller units, useful for languages with complex morphology or for generating robust word representations. In this example, "Unsupervised" is split into "Un" and "supervised," providing more granularity in representation compared to traditional word tokenization.

## NLTK Tokenizers

NLTK provides these types of tokenizers:

1. `word_tokenize()`: This function splits text into individual words or tokens.
2. `sent_tokenize()`: This function splits text into sentences based on punctuation marks such as periods, exclamation marks, and question marks. This function ensures that each sentence is treated as a separate unit of analysis.
3. `TweetTokenizer()`: This function is designed specifically for processing social media texts, which often contain hashtags, mentions, and emoticons.
4. `RegexpTokenizer()`: This tokenization is based on regular expressions, allowing users to define custom patterns for token boundaries.
5. `WhitespaceTokenizer()`: This function is based on whitespace characters, useful for cases where text is already preprocessed or structured.