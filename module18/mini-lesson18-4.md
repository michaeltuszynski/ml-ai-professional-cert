# Mini-Lesson 18.4: Named Entities and Tokenization

## Part-of-Speech Tagging (POS Tagging)

**Definition:** Part-of-speech (POS) tagging involves assigning labels to each word in a sentence based on its role in the sentence (noun, verb, adjective, etc). This helps in understanding the grammatical structure and meaning of the text.

### Example:

Sentence: "The quick brown fox jumps over the lazy dog."

POS Tags:
- "The" (Determiner - DT)
- "quick" (Adjective - JJ)
- "brown" (Adjective - JJ)
- "fox" (Noun - NN)
- "jumps" (Verb - VBZ)
- "over" (Preposition - IN)
- "the" (Determiner - DT)
- "lazy" (Adjective - JJ)
- "dog" (Noun - NN)

In this tagging, each word is labeled to show its grammatical role, which helps in understanding the structure of the sentence.

## Named Entity Recognition (NER)

**Definition:** Named entity recognition involves identifying and classifying entities in text into predefined categories (names, organizations, locations, dates, etc). This is useful for extracting specific information from text.

### Example:

Sentence: "Apple Inc. was founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in Cupertino."

NER Tags:
- "Apple Inc." (Organization - ORG)
- "Steve Jobs" (Person - PERSON)
- "Steve Wozniak" (Person - PERSON)
- "Ronald Wayne" (Person - PERSON)
- "Cupertino" (Location - GPE)

NER helps in identifying that "Apple Inc" is an organization, "Steve Jobs" is a person, and "Cupertino" is a location.

## Stemming

**Definition:** Stemming is the process of reducing a word to its base or root form, often by removing suffixes or prefixes. This can help in normalizing words so that different forms of a word are treated as the same.

### Example:

Words: "running," "runner," "runs"

Stemmed Form: "run"

In stemming, different forms of the word "run" are reduced to the common root form "run," allowing the system to treat all variations as equivalent.

## Lemmatization

**Definition:** Lemmatization is the process of reducing words to their base or dictionary form, considering the word's context and its part of speech. Unlike stemming, lemmatization uses vocabulary and morphological analysis to return the base or canonical form of a word.

### Example:

Words: "running," "ran," "runs"

Lemmatized Form:
- "running" → "run"
- "ran" → "run"
- "runs" → "run"

In lemmatization, "running," "ran," and "runs" are all reduced to "run," but the process ensures that "run" is a valid word in the language, considering its context and grammatical role.

## Summary

1. **POS Tagging:** POS tagging assigns grammatical labels to words in a sentence. It uses NLTK to tag parts of speech for each word in a sentence.
2. **NER:** NER identifies and classifies named entities into categories such as persons, organizations, and locations. It uses spaCy to recognize and classify named entities in a text.
3. **Stemming:** Stemming reduces words to their root form, often resulting in non-dictionary words. It uses NLTK's PorterStemmer to reduce words to their root form.
4. **Lemmatization:** Lemmatization reduces words to their base or dictionary form, considering their context and part of speech. It uses spaCy to reduce words to their base form considering context.