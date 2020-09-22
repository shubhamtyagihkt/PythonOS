# once file is opened it needs to be closed
# opening file
file = open("poem.txt")
# doing read
print(file.readline())
print()
print(file.read())
# closing file
file.close()

print()
print()
print("Method 2 'with open' ")
print()

with open("poem.txt") as file:
    print(file.readline())
    print(file.readline())

# with open automatically closes file after use
