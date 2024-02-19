import re

# Regular Expressions
sample_string = "The quick brown fox jumps over the lazy dog near the bank of the river"

# Searching

# r'' is a regex string, which contains the regex
search_regex = r'[aeiou]'
search_num = r'[0123456789]'
search_num2 = r'[0-9]'
search_alph = r'[a-zA-Z]'
regex_woodchuck = r'wooduck'
regex_not = r'[^a-z]'

# findall parameters
# regex formula, string to search
# search function params same with findall
find_res = re.findall(regex_not, sample_string)
print(find_res)

search_res = re.search(search_regex, sample_string)
print(search_res)

# Text Processing
# Casing
# Lower case
sent_lower = sample_string.lower()
print(sent_lower)

# Upper case
sent_upper = sample_string.upper()
print(sent_upper)

# Title case
sent_case = sample_string.title()
print(sent_case)

# Sentence case
sent_cap = sample_string.capitalize()
print(sent_cap)

# Punctuation removal
sent_with_puncs = "Lorem ipsum dolor sit amet, platonem deseruisse vix ne? In per dictas accusam rationibus. Duo ut ullamcorper philosophia! Hinc agam te cum. Id vix modo eligendi similique, dicant fuisset mentitum mei te, legimus fuisset eu sit? Ut mei viderer perpetua postulant."
# regex to remove punctuations
regex_puncs = r'[?,.!]'

# sub refers to substitute
# 3 parameters
# regex pattern, the replacement string, the sentence with punctuations
# removing characters means the replacement is just ""
puncs_rmv = re.sub(regex_puncs, '' , sent_with_puncs)
print(puncs_rmv)

# Diacritic removal

# Number to words
from num2words import num2words
sample_num = 541
num_words = num2words(sample_num)
print(num_words)

# Expanding Contractions
import contractions
