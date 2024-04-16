# install the vaderSentiment module first
# before running this code

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# create an instance of the analyzer
sa = SentimentIntensityAnalyzer()
# lexicon used by vader, tokens accompanied by their values
# used for measuring sentiment
print(sa.lexicon)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# run vader on a string value
# vader has a custom stemmer/lemmatizer so that it will match the lexicon
sample_input = "Python is very readable and it's great for NLP."
print(sa.polarity_scores(text=sample_input))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

sample_input = "Python is not a bad choice for most applications"
print(sa.polarity_scores(text=sample_input))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# emulate corpus
corpus = [
    "Horrible! Completely useless. :(",
    "It was OK. Some good and some bad things."
]

for doc in corpus:
    scores = sa.polarity_scores(doc)
    print('{:+}: {}'.format(scores['compound'], doc))