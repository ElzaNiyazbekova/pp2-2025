import os

path = "C:/usr/local/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/homebrew/bin:/opt/homebrew/sbin:/Library/Frameworks/Python.framework/Versions/3.10/bin" 

print("Directories:")
for entry in os.listdir(path):
    if os.path.isdir(os.path.join(path, entry)):
        print(entry)

print("Files:")
for entry in os.listdir(path):
    if os.path.isfile(os.path.join(path, entry)):
        print(entry)

print("All Directories and Files:")
for entry in os.listdir(path):
    print(entry)