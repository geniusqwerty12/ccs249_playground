# Before running this, make sure that the 2 files kite_text.txt and kite_history are
# on the same folder as this file

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()

term = "kite"
term2 = "china"

# Read the kite intro and history
with open("kite_text.txt", "r") as file:
    # Prepare the documents
    kite_intro = file.read().lower()
    intro_tokens = tokenizer.tokenize(kite_intro)

with open("kite_history.txt", "r") as file:
    kite_history = file.read().lower()
    history_tokens = tokenizer.tokenize(kite_history)


intro_total = len(intro_tokens)
history_total = len(history_tokens)

print("Total length of words in Intro: ", intro_total)
print("Total length of words in History: ", history_total)

# For term frequency
intro_tf = {}
history_tf = {}

from collections import Counter

intro_counts = Counter(intro_tokens)
history_count = Counter(history_tokens)

# Get the frequency of the word stated above
intro_tf[term] = intro_counts[term] / intro_total
history_tf[term] = history_count[term] / history_total

intro_tf[term2] = intro_counts[term2] / intro_total
history_tf[term2] = history_count[term2] / history_total

print("~~~~~~ Term Frequency ~~~~~~~~~")

print(f'Term frequency of {term} in the intro document: {intro_tf[term]}')
print(f'Term frequency of {term} in the history document: {history_tf[term]}')

print(f'Term frequency of {term2} in the intro document: {intro_tf[term2]}')
print(f'Term frequency of {term2} in the history document: {history_tf[term2]}')

# Get the value of the IDF of the term with respect to the documents
number_docs = 2

term_count = {}
term_count[term] = 0
term_count[term2] = 0

for doc in [intro_tokens, history_tokens]:
    if term in doc:
        term_count[term] += 1
    if term2 in doc:
        term_count[term2] += 1

# IDF
intro_idf = {}
history_idf = {}

# intro_idf[term] = number_docs / term_count[term]
# intro_idf[term2] = number_docs / term_count[term2]

from math import log

# applying log of 10
intro_idf[term] = log(number_docs / term_count[term])
intro_idf[term2] = log(number_docs / term_count[term2])

history_idf[term] = number_docs / term_count[term]
history_idf[term2] = number_docs / term_count[term2]

print("~~~~~~ Inverse Document Frequency ~~~~~~~~~")

print(f" IDF for '{term}' word in intro document: {round(intro_idf[term], 4)}")
print(f" IDF for '{term}' word in history document: {round(history_idf[term], 4)}")

print(f" IDF for '{term2}' word in intro document: {round(intro_idf[term2], 4)}")
print(f" IDF for '{term2}' word in history document: {round(history_idf[term2], 4)}")

# TF-IDF
intro_tfidf = {}
history_tfidf = {}

intro_tfidf[term] = intro_tf[term] * intro_idf[term]
history_tfidf[term] = history_tf[term] * history_idf[term]

intro_tfidf[term2] = intro_tf[term2] * intro_idf[term2]
history_tfidf[term2] = history_tf[term2] * history_idf[term2]


print("~~~~~~ Term Frequency - Inverse Document Frequency ~~~~~~~~~")
print(f" TF-IDF for '{term}' word in intro document: {round(intro_tfidf[term], 4)}")
print(f" TF-IDF for '{term}' word in history document: {round(history_tfidf[term], 4)}")

print(f" TF-IDF for '{term2}' word in intro document: {round(intro_tfidf[term2], 4)}")
print(f" TF-IDF for '{term2}' word in history document: {round(history_tfidf[term2], 4)}")