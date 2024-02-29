from nltk.stem import PorterStemmer
 
# Create a Porter Stemmer instance
porter_stemmer = PorterStemmer()
 
# Example words for stemming
words = ["running", "jumps", "happily", "running", "happily"]
 
# Apply stemming to each word
stemmed_words = [porter_stemmer.stem(word) for word in words]
 
# Print the results
print("Original words:", words)
print("Stemmed words:", stemmed_words)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from nltk.stem import SnowballStemmer
 
# Choose a language for stemming, for example, English
stemmer = SnowballStemmer(language='english')
 
# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply Snowball Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]
 
# Print the results
print("Original words:", words_to_stem)
print("Stemmed words:", stemmed_words)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from nltk.stem import LancasterStemmer
 
# Create a Lancaster Stemmer instance
stemmer = LancasterStemmer()
 
# Example words to stem
words_to_stem = ['running', 'jumped', 'happily', 'quickly', 'foxes']
 
# Apply Lancaster Stemmer
stemmed_words = [stemmer.stem(word) for word in words_to_stem]
 
# Print the results
print("Original words:", words_to_stem)
print("Stemmed words:", stemmed_words)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from nltk.stem import RegexpStemmer
 
# Create a Regexp Stemmer with a custom rule
custom_rule = r'ing$'
regexp_stemmer = RegexpStemmer(custom_rule)
 
# Apply the stemmer to a word
word = 'running'
stemmed_word = regexp_stemmer.stem(word)
 
print(f'Original Word: {word}')
print(f'Stemmed Word: {stemmed_word}')