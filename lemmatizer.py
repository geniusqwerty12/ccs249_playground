# load the lemmmatizer from the nltk
from nltk.stem import WordNetLemmatizer

# create an instance of the lemmatizer
lemmatizer = WordNetLemmatizer()

# sample lemmatization
print(lemmatizer.lemmatize("better"))

# get the base word of better
# if it was used as an adjective
# the pos parameter refers to the
# part of speech that the will refer

print(lemmatizer.lemmatize("better", pos="a"))