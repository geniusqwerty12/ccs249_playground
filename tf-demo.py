from nltk.corpus import brown

# built in method that returns a tokenized corpus
print(brown.words()[:10])

print(len(brown.words()))


from collections import Counter
# Removing punctuations
puncs = set((',', '.', '--', '-', '!', '?', ':', ';', '``', "''", '(', ')', '[',']'))
# Tokenization
word_list = ( x.lower() for x in brown.words() if x not in puncs)
# Creating a BOW
token_counts = Counter(word_list)
# Listing the top 20 frequent words in the Brown corpus
# Term Frequency (not normalized)
# Rank 1 in term frequency appears twice as much as the 2nd rank term
print(token_counts.most_common(20))
