# create a new file called
# corpora.py, and copy the 
# codes below

# run the nltk-scripy file and download all of the corporas
import nltk.corpus as corpus

# print(corpus.brown.raw())

# list the file ids, name of files that contains
# the words
print(corpus.abc.fileids())
print(corpus.genesis.fileids())
print(corpus.gutenberg.fileids())

# # You can access each of the file
# print(corpus.gutenberg.raw("chesterton-thursday.txt"))
# # print(corpus.abc.words("rural.txt"))
# list = corpus.brown.words("cr07")
# print(list)

# corpora_name = ["brown", "genesis", "gutenberg"]
# corpora = [corpus.brown, corpus.genesis, corpus.gutenberg]

# nameIndex = 0
# for corp in corpora: 
#     file_list = corp.fileids()
#     words = corp.words(file_list[0])
#     for i in range(10):
#         print(f'Corpus {corpora_name[nameIndex]} with the file name {file_list[0]} contains the text {words[i]} at index {i}')

#     nameIndex += 1
#     print('~~~~~~~')