filename = 'r.txt'
file_path = '/Users/elzaniyazbekova/Desktop/pp2/lab6/dir/r.txt'

with open(file_path, 'r') as file:
    num_lines = 0
    for line in file:
        num_lines += 1

print(f'The number of lines in {filename} is: {num_lines}')