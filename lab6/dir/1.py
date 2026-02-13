import os

# path = "/Users/elzaniyazbekova/Desktop/pp2/lab6/dir" 
# f=open("/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/r.txt", "r")
# print(f.readline().rstrip())
# f.close
# print(f.readline().rstrip())
# print("Directories:")
# for entry in os.listdir(path):
#     if os.path.isdir(os.path.join(path, entry)):
#         print(entry)

# print("Files:")
# for entry in os.listdir(path):
#     if os.path.isfile(os.path.join(path, entry)):
#         print(entry)

# print("All Directories and Files:")
# for entry in os.listdir(path):
#     print(entry)


# print ("Directory")
# for p in os.listdir(path):
#     if os.path.isdir(os.path.join(path, p)):
#         print(p)

# print("Files")
# for p in os.listdir(path):
#     if os.path.isfile(os.path.join(path, p)):
#         print(p)
#     for e in os.path.isfile():


# print("All Directories and Files")
# for p in os.listdir(path):
#     print(p)

# largest_file = None
#     max_size = 0

#     for file in os.listdir(directory):  # Перебираем файлы в папке
#         file_path = os.path.join(directory, file)  # Полный путь к файлу
#         if os.path.isfile(file_path):  # Проверяем, что это файл, а не папка
#             size = os.path.getsize(file_path)  # Получаем размер файла
#             if size > max_size:  # Если нашли файл больше текущего максимума
#                 max_size = size
#                 largest_file = file_path

#     return largest_file, max_size

# entries = os.listdir(path)

# for i in entries:
#     full_path = os.path.join(path,i)
#     if os.path.isfile(full_path):
#         print(os.path.getsize(full_path))
# for i in entries:
#     f = os.path.join(path,i)
#     if os.path.isfile(f):
#         print(os.path.getsize(f))

# for i in entries:
#     f = os.path.join(path, i)
#     if os.path.isfile(f):
#         print(os.path.getsize(f))






import re



a = input("Enter")
p = r"[A-Z][a-z][0-9][!@#$%^&*()_/-]{3}"
# if len(a)<8
#     print("Too many symbols")

print(re.search(p, a))






