# basic matching with grep in command line
# $ grep regex file

# if want to ignore case
# $ grep regex file


import re

# python string 
string = "this is string"
# python rawstring  
rawstring = r"this is rawstring"
# rawstring assumes \ (backslash) as regular character not as escape sequence

# simple matching
print(re.search(r"^x", "xenon"))
# case sensitive matching
print(re.search(r"^x", "Xenon", re.IGNORECASE))
# search patterns
# ^ => indicate the start of line
# $ => indicate end of the line
# . => wildcard - matches any character
# ? => matches zero of one previous character
# * => matches zero or more previous character
# + => matches one or more previous character
# [] => define any range of characters or individual characters to match
# [^] => matches everything except letter in square brackets followed after ^

# using . to match any character
print(re.search(r"p.ng", "ping"))
print(re.search(r"p.ng", "pong"))


# Character classes using []
print(re.search(r"[Pp]ython", "Python, pythonic"))
print(re.search(r"[Pp]ython", "pythonic, Python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# pattern that are not in group
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))

# using or | in regex
print(re.search(r"cat|dog", "dog"))
print(re.search(r"cat|dog", "cat"))


# search function only finds one match 
# find all finds all matching patterns
print(re.findall(r"cat|dog", "Both cat and dog are good"))

# REPETIION (GREEDY)
print(re.search(r"h.*o", "hellololo"))

# REPETITION (NON-GREEDY)
print(re.search(r"h.*?o", "hellololo"))


# $ egrep command have two more characters + , ? it make it even more powerful
 
print(re.search(r"p?ython", "python"))
print(re.search(r"p?ython", "ython"))


# ESCAPING CHARACTERS in regex (\)
# match one of the special characters

print(re.search(r"\.com", "google.com"))

# why we use rawstrings
# to prevent \n \t like confusion with regex escape characters
# these will be treated like the literal characters that is written

# some regex escape sequences are
# \w => matches any alphanumeric character and  _(underscore)
# \d => matches digit
# \s => matches white space characters

# Validating patter for variabla name qualifier in python

pattern = r"^[a-zA-Z_][\w]*$"

print(re.search(pattern, "_this_is_valid"))
print(re.search(pattern, "this is not"))
print(re.search(pattern, "a9"))
print(re.search(pattern, "9a"))



