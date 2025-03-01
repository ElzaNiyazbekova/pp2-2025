import re

# s=str(input("enter "))
# print(re.search('^ab*',s))
#2

# string = input('Enter ')

# pattern = r'a[bb]{2,3}'

# if re.search(pattern, string):
#     print("Match found")
# else:
#     print('Match not found')

#3
# text = input('Enter ').split(",")
# pattern = r"[a-z][_]"

# for i in text:
#     if re.search(pattern, i):
#         print(i)

#4

# text = input('Enter ').strip()

# pattern = r"[A-Z][a-z]+"

# matches = re.findall(pattern, text)

# print(matches)

#5
# pattern = r'a.*b$'

# strings = input('Enter ').split(",")

# for string in strings:
#     if re.match(pattern, string):
#         print(f"{string} matches ")
#     else:
#         print(f"{string} does not ")

#6
# text = input('Enter:')

# text = text.replace(" ", ":").replace(",", ":").replace(".", ":")

# print(text)

#7
# s = input('Enter ')
# b = ''
# for i in range(len(s)):
#     if s[i]!='_':
#         b+=s[i]
#     elif s[i]=='_':
#         b+=s[i+1].upper()
# print(b)
#8
# t= input('Enter ')

# s = re.findall('[A-Z][^A-Z]*', t)

# print(s)

#9

# t= input('Enter ')

# n = re.sub(r"(\w)([A-Z])", r"\1 \2", t)

# print(n)

#10
# s = input('Enter ')
# b = ''
# for i in range( len(s) ) :
#     if s[i].isupper()!= True:
#         b+=s[i]
#     elif s[i].isupper()==True:
#         b+='_'+s[i].lower()

# print(b)
