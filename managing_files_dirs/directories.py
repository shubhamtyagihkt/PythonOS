# get current working direcotry
# $ pwd
# on linux

import os

print(os.getcwd())

# make new directory
if not os.path.exists("hi"):
    os.mkdir("hi")

# change current working directory

os.chdir("hi")

print(os.getcwd())

os.chdir("../")

# remove dir
# works only when no files or subdirectory contained in it
os.rmdir("hi")


# get list of all directory and file 

print(os.listdir("./"))


# see all in action

dir = "./"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if (os.path.isdir(fullname)):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))
