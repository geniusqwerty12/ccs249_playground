import nltk.corpus as corpus
import re

list = corpus.abc.raw("rural.txt")

# remove punctuations
punc_regex = r'[.!,.:\n]'
list = re.sub(punc_regex, "", list)


# split using delimiter
split_res = list.split(" ")
print(len(split_res))
list_words = corpus.abc.words("rural.txt")
print(len(list_words))


for i in range(50, 100, 1):
    print(i, ": ", split_res[i], " vs ", list_words[i])
    print("is equal: ", split_res[i] == list_words[i])

# check the total length
print(len(split_res))
print(len(list_words))