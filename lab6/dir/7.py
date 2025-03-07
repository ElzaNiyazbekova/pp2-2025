with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/m.txt", "r") as source_file:
    c= source_file.read()

with open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/r.txt", "w") as destination_file:
    destination_file.write(c)