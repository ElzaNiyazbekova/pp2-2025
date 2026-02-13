import os

path = "/Users/elzaniyazbekova/Desktop/pp2/lab5"  

if os.path.exists(path):
    print("Path exists")
    directory, filename = os.path.split(path)
    print("Directory:", directory)
    print("Filename:", filename)
else:
    print("Path does not exist")

if os.path.exists(path):
    print("Path exists")
    di, file = os.path.split(path)

        