my_list = ['a', 'b', 'c', 'd']

with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/m.txt", "w") as file:
    for item in my_list:
        file.write(item + "\n")

with open("/Users/elzaniyazbekova/Desktop/", "w") as file:
    for i in my_list:
        file.write(i + "\n")