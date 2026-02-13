import string

letters = string.ascii_uppercase

for letter in letters:
    filename = letter + ".txt"
    with open(filename, "w") as file:
        file.write("This is file " + letter + ".txt")
