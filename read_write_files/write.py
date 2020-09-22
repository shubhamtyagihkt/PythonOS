
# flags to use
# w = write to file (flush file at inclusion time / create new file if !file)
# a = write to file at the end
# r+ = perform both read and write

with open("poem.txt", "a") as file:
    file.write("""hello""")