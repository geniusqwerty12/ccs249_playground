from nltk.tokenize import TreebankWordTokenizer

sentence = """
    The faster Harry got to the store,
    the faster Harry would get home.
"""
tokenizer = TreebankWordTokenizer()
tokens = tokenizer.tokenize(sentence.lower())
print(tokens)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


from collections import Counter
# use the Counter class to get
# the unique words and count them
bag_of_words = Counter(tokens)
print(bag_of_words)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# you can set the limit
# in this case up to 4 common worrds
print(bag_of_words.most_common(4))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# get the count of the unique word
times_harry_appears = bag_of_words['harry']
# get the total number of unique words from the original source
num_unique_words = len(bag_of_words)

tf = times_harry_appears / num_unique_words
print("Frequency of the word Harry", round(tf, 4))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# frequency vector
document_vector = []
doc_length = len(tokens)
for key, value in bag_of_words.most_common():
    document_vector.append(value / doc_length)

print(document_vector)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# create a corpus
docs = ["The faster Harry got to the store, the faster and faster Harry would get home."]
docs.append('Harry is hairy and faster than Jill.')
docs.append('Jill is not as hairy as Harry.')

doc_tokens = []
for doc in docs:
    # tokenize each item in the docs list
    doc_tokens += [sorted(tokenizer.tokenize(doc.lower()))]
    
# check the first item
print(len(doc_tokens[0]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# add the count of each words in each item
all_doc_tokens = sum(doc_tokens, [])
print(len(all_doc_tokens))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
lexicon = sorted(set(all_doc_tokens))
print(lexicon)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# initialize the vector, assigning each token to 0 count
from collections import OrderedDict
zero_vector = OrderedDict((token, 0) for token in lexicon)
print(zero_vector)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# copy the base vector, then update the values of the vector
import copy
doc_vectors = []
for doc in docs:
    # copy() creates and independent copy
    # separate instance of the zero vector
    vec = copy.copy(zero_vector)
    tokens = tokenizer.tokenize(doc.lower())
    token_counts = Counter(tokens)
    for key, value in token_counts.items():
        vec[key] = value / len(lexicon)
    doc_vectors.append(vec)
print(doc_vectors)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
import math
def cosine_sim(vec1, vec2):
    # convert the dictionaries
    # to lists for easier matching
    vec1 = [val for val in vec1.values()]
    vec2 = [val for val in vec2.values()]

    dot_prod = 0
    for i, v in enumerate(vec1):
        dot_prod += v * vec2[i]
    
    mag_1 = math.sqrt(sum([x**2 for x in vec1]))
    mag_2 = math.sqrt(sum([x**2 for x in vec2]))

    return dot_prod / (mag_1 * mag_2)