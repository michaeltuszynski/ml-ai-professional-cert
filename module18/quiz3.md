# NLP Operations Quiz

## Question 1 (1 point)
Which of the following statements accurately describes normalization operations in NLP?

**Options:**
1. Normalization operations take tokens as input and produce tokens as output.
2. Normalization operations take numerical vectors as input and produce tokens as output.
3. Normalization operations take tokens as input and produce raw text as output.
4. Normalization operations take raw text as input and produce numerical vectors as output.

**Answer:** Option 1: Normalization operations take tokens as input and produce tokens as output.
> Explanation: Normalization operations are text-to-text transformations that standardize tokens while preserving their fundamental meaning. Examples include case folding, lemmatization, and stemming. These operations work at the token level, taking tokens as input and outputting normalized tokens.

---

## Question 2 (1 point)
Which of the following is NOT a stop word?

**Options:**
1. am
2. is
3. natural
4. are

**Answer:** Option 3: natural
> Explanation: Stop words are common, functional words that typically don't carry significant meaning (like articles, prepositions, and auxiliary verbs). "Natural" is a content word (adjective) that carries semantic meaning, while "am", "is", and "are" are all forms of the verb "to be" and are classic examples of stop words.

---

## Question 3 (1 point)
What does the function `pos_tag(words)` in NLTK do?

**Options:**
1. It computes the frequency distribution of words in a list.
2. It tokenizes a list of words into sentences.
3. It translates a list of words into multiple languages.
4. It converts a list of words into a list of their corresponding part-of-speech tags.

**Answer:** Option 4: It converts a list of words into a list of their corresponding part-of-speech tags.
> Explanation: The `pos_tag()` function in NLTK is specifically designed for part-of-speech tagging. It takes a list of tokens as input and returns a list of tuples, where each tuple contains a word and its corresponding POS tag (e.g., noun, verb, adjective, etc.).

---

## Question 4 (1 point)
What would the output be if you applied stemming to the following list of words: {joy, joyful, joyfully, joyous}?

**Options:**
1. {joy, joyfull, joyfull, joyus}
2. {joy, joy, joy, joy}
3. {joy, joy, joyfull, joyus}
4. {joy, joyful, joyfully, joyous}

**Answer:** Option 2: {joy, joy, joy, joy}
> Explanation: Stemming reduces words to their root or base form (stem) by removing affixes. A stemmer would reduce all variations of "joy" (joyful, joyfully, joyous) to their common stem "joy", resulting in identical outputs for all four words.

---

## Answer Key
1. Option 1 - Normalization operations take tokens as input and produce tokens as output (Core definition of token-to-token transformations)
2. Option 3 - "natural" (Content word vs. functional stop words)
3. Option 4 - POS tagging function (Core NLTK functionality for grammatical analysis)
4. Option 2 - All words reduce to "joy" (Basic stemming behavior removing all affixes)