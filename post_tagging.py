import nltk
from collections import Counter

text = "The quick brown fox jumps over the lazy dog near the river."

# perform lowercase
text_lowercase = text.lower()

# tokenize the text
tokens = nltk.word_tokenize(text_lowercase)

print("Tokens: ", tokens)

# Apply PoS Tagging using NLTK
# this uses a rule-based method
tags = nltk.pos_tag(tokens)
print("Tokens tagged with PoS: ", tags)

# use the Counter module to get the count of PoS tags with their tokens
pos_count = Counter( tag for word, tag in tags)
print("Counted PoS tags: ", pos_count)

# for statistical/probabilistic models for PoS
# you can use the Spacy module
import spacy

# Before running the code, run the command below:
# python -m spacy download en
# Load the model 'en_core_web_sm'
nlp = spacy.load('en_core_web_sm')

new_sentence = "Probabilistic models are underrated, as they are simple but gives results with high accurary"

# process the input using the spaCy's NLP pipeline
doc = nlp(new_sentence)

# Check the result of the tagging
for token in doc:
    print(token.text,' => ', token.pos_)