import os
# get file size
print(os.path.getsize("helloji.txt"))

# get last modified time
print(os.path.getmtime("helloji.txt"))

# more human readable
import datetime

timestamp = os.path.getmtime("helloji.txt")
print(datetime.datetime.fromtimestamp(timestamp))

# get absolute path
print(os.path.abspath("helloji.txt"))