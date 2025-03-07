my_list = ["apple", "banana", "cherry", "date"]

with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/m.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")