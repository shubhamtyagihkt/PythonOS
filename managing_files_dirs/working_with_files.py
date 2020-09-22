import os

if os.path.exists("temp.txt"):
    os.remove("temp.txt")

if os.path.exists("hello.txt"):
    os.rename("hello.txt", "helloji.txt")