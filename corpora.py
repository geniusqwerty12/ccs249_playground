# run the nltk-scripy file and download all of the corporas
import nltk.corpus as corpus

# list the file ids, name of files that contains
# the words
print(corpus.brown.fileids())

# You can access each of the file
print(corpus.brown.words("cr07"))