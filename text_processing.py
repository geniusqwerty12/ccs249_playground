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
regex_kleenes = r'Th*'
regex_kleenep = r'Th+'
regex_wildcard = r'T.e'

# findall parameters
# regex formula, string to search
# search function params same with findall
find_res = re.findall(regex_kleenep, sample_string)
print(find_res)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
search_res = re.search(search_regex, sample_string)
print(search_res)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Text Processing
# Casing
# Lower case
sent_lower = sample_string.lower()
print(sent_lower)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Upper case
sent_upper = sample_string.upper()
print(sent_upper)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Title case
sent_case = sample_string.title()
print(sent_case)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Sentence case
sent_cap = sample_string.capitalize()
print(sent_cap)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
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
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Diacritic removal
from unicodedata import normalize
rmv_dia = normalize('NFD', 'café')
print(rmv_dia)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Number to words
from num2words import num2words
sample_num = 541
num_words = num2words(sample_num)
print(num_words)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# Expanding Contractions
import contractions

contr_str = "I'll"
exp_str = contractions.fix(contr_str)
print(contr_str, " expanded to: ", exp_str)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
contr_text = '''I'll be there within 5 min. Shouldn't you be there too? 
          I'd love to see u there my dear. It's awesome to meet new friends.
          We've been waiting for this day for so long.'''

exp_st = contractions.fix(contr_text)
print(contr_text, " expanded to: ", exp_st)
