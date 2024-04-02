import nltk.corpus as corpus
import re

# list = corpus.abc.raw("rural.txt")
# rmv_linebreaks = r'[\n]'
# list = re.sub(rmv_linebreaks, " ", list)

# #  split using delimiter
# split_res = list.split(" ") # list
# print(len(split_res))
# list_words = corpus.abc.words("rural.txt")
# print(len(list_words))

# for i in range(30, 50, 1):
#     print(i, ": ", split_res[i], " vs ", list_words[i])
#     print("is equal: ", split_res[i] == list_words[i])


from nltk.stem import PorterStemmer
 
# Create a Porter Stemmer instance
porter_stemmer = PorterStemmer()
 
# Example words for stemming
words_1 = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply stemming to each word
stemmed_words_1 = [porter_stemmer.stem(word) for word in words_1]

# Similar to:
# stemmed_words = []
# for word in words_1:
#     stemmed_words.append( porter_stemmer.stem(word) )

# Print the results
print("Original words:", words_1)
print("Stemmed words:", stemmed_words_1)


# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from nltk.stem import SnowballStemmer
 
# Choose a language for stemming, for example, English
stemmer_2 = SnowballStemmer(language='english')
 
# Example words to stem
words_to_stem_2 = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply Snowball Stemmer
stemmed_words_2 = [stemmer_2.stem(word) for word in words_to_stem_2]
 
# Print the results
print("Original words:", words_to_stem_2)
print("Stemmed words:", stemmed_words_2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from nltk.stem import LancasterStemmer
 
# Create a Lancaster Stemmer instance
stemmer_3 = LancasterStemmer()
 
# Example words to stem
words_to_stem_3 = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply Lancaster Stemmer
stemmed_words_3 = [stemmer_3.stem(word) for word in words_to_stem_3]
 
# Print the results
print("Original words:", words_to_stem_3)
print("Stemmed words:", stemmed_words_3)

# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
from nltk.stem import RegexpStemmer
 
# Create a Regexp Stemmer with a custom rule
custom_rule = r'ing$|ning$' # OR # words that end with ning
regexp_stemmer = RegexpStemmer(custom_rule)
 
# Apply the stemmer to a word
word_4 = 'running' # sing
stemmed_word_4 = regexp_stemmer.stem(word_4)
 
print(f'Original Word: {word_4}')
print(f'Stemmed Word: {stemmed_word_4}')