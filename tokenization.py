sentence = "Thomas Jefferson began building Monticello at the age of 26."
split_words = sentence.split()
# print(split_words)

import numpy as np

# quick and dirty tokenizer
token_sequence = str.split(sentence)

# vocab list all the unique tokens that you want to keep track of
vocab = sorted(set(token_sequence))

# sorted lexographically so numbers come before letters and capital letters
# come before lowercase letters
print(', '.join(vocab))

# get the number of tokens
num_tokens = len(token_sequence)
vocab_size = len(vocab)

# converting textual to numerical data
# create an array
# Empty table created using numpy, as wide as your count of unique
# vocabulary terms and as high as the length of your documents
onehot_vectors = np.zeros((num_tokens, vocab_size), int)

# for each word in the sentence, mark the column for that word in your vocabulary with a 1
for i, word in enumerate(token_sequence):
    onehot_vectors[i, vocab.index(word)] = 1

# for each
print(', '.join(vocab))

print(onehot_vectors)

import pandas as pd

data = pd.DataFrame(onehot_vectors, columns=vocab)
print(data)

import re
sentence2 = """Thomas Jefferson began building
Monticello at the \n
... age of 26."""

# Splits the sentence on whitespace or punctuation
# that occurs at least once
token = re.split(r'[-\s.,;!?]+', sentence2)
print(token)

# compiling regex
pattern = re.compile(r"([-\s.,;!?])+")
tokens = pattern.split(sentence)
print(tokens)

# using NLTK
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')
token_res = tokenizer.tokenize(sentence)
print(token_res)

from nltk.tokenize import TreebankWordTokenizer
sentence3 = """Monticello wasn't designated as UNESCO World Heritage
... Site until 1987."""
tokenizer_tree  = TreebankWordTokenizer()
tree_res = tokenizer_tree.tokenize(sentence3)
