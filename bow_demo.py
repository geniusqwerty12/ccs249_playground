from collections import Counter
from nltk.tokenize import TreebankWordTokenizer
# ditch stopwords
from nltk import corpus

tokenizer = TreebankWordTokenizer()

# get the document
# either from the module
# from nlpia.data.loaders import kite_text

# or load the text from a file
with open("kite_text.txt", "r") as file:
    kite_data = file.read().replace("\n", " ")

    tokens = tokenizer.tokenize(kite_data.lower())
    token_counts = Counter(tokens)

    # presence of stopwords
    print(token_counts)

    # ditch the stopwords
    stopwords = corpus.stopwords.words('english')

    # update the tokens - remove/filter stopwords
    tokens = [x for x in tokens if x not in stopwords]

    kite_counts = Counter(tokens)
    print(kite_counts)