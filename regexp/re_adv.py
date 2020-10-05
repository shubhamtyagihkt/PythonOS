# CAPTURING GROUPS => portion of pattern enclosed in paranthesis
import re
result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result)

print(result.groups())

print(result[0])
print(result[1])
print(result[2])

"{}, {}".format(result[2], result[1])


# More on REPETITION QUALIFIERS => specifying number of times the pattern to repeat
# {} => used to specify number of times pattern to repeat
print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))

# What if we want to match those words that have exactly 5 characters only
# we can use \b indicate word limit at the begginning and end of words

print(re.findall(r"\b[a-zA-Z]{5}\b", "a scary ghost appeared"))

# specify range of letters to be considererd

print(re.findall(r"\w{5,10}", "I really like strawberry asdfasdfasfaf"))

# min 5 characters
print(re.findall(r"\w{5,}", "I really like strawberry asdfasdfasfaf"))

#!/usr/bin/env python3

import csv

def read_employee(csv_file_location):
        with open(csv_file_location) as file:
                dict_reader = csv.DictReader(file)
                # there is not standard way to define csv
                # so the parser need to be flexible
                # for  thi swe use dialect property
                csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
                # this dailct remove any leading spaces while parsing
                emp_file = csv.DictReader(file, dialect = 'empDialect')
                employee_list = []
                for data in emp_file:
                        employee_list.append(data)
                return employee_list
