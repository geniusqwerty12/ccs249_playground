from nltk.corpus import brown

# built in method that returns a tokenized corpus
print(brown.words()[:10])

# Part of Speech Tagging
print(brown.tagged_words()[:5])

print(len(brown.words()))


from collections import Counter
# Removing punctuations
puncs = set((',', '.', '--', '-', '!', '?', ':', ';', '``', "''", '(', ')', '[',']'))
# Tokenization
word_list = ( x.lower() for x in brown.words() if x not in puncs)
# Creating a BOW
token_counts = Counter(word_list)
# Listing the top 20 frequent words in the Brown corpus
print(token_counts.most_common(20))

