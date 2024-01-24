import re # regular expression

r = "(hi|hello|hey)[ ]*([a-z]*)"
# Simple Tests for the Regex created
print(re.match(r, 'Hello Rosa', flags=re.IGNORECASE))

print(re.match(r, "hi ho, hi ho, it's off to work...", flags=re.IGNORECASE))

print(re.match(r, "hey, what's up", flags=re.IGNORECASE))

# Complex test for the regex
r1 = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[])?(morn[gin']{0,3}|afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
# need to compile first because r1 is not a regular expression, it is raw text
re_greeting = re.compile(r, flags=re.IGNORECASE)
print(re_greeting.match('Hello Rosa'))
print(re_greeting.match('Hello Rosa').groups())
print(re_greeting.match('Good morning Rosa'))
print(re_greeting.match('Good Manning Rosa'))
print(re_greeting.match('Good evening Rosa Parks').groups())
print(re_greeting.match("Good Morn'n Rosa"))
print(re_greeting.match('yo Rosa'))