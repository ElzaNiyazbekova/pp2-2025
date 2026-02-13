import re
txt = "The rain in Spain"
print((re.search(" \w+ai\w+", txt)))
# print(re.findall("\w+ai\w+$", txt))
# s=str(input("enter "))
# print(re.search('^ab*',s))
#2

# string = input('Enter ')

# pattern = r'a[bb]{2,3}'


# if re.search(pattern, string):
#     print("Match found")
# else:
#     print('Match not found')
# print(re.search('a[bb]{2,3}',string))
#3

# text = input('Enter ').split(",")
# p=r"[a-z][_]"

# for i in text:
#     if re.search(p, i):
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



a = input('Enter ').split(',')
b = ' '
r = r'^A.*b$'
for i in a:
    if re.match(r, i):
        b+= i 
print(b)
# print(re.findall("^A.*b$", a))
# print(re.search("^ab*", a))
# print(re.search("ab{2,3}", a))

# p = r"[a-z][_]"
# for i in a:
#     if re.search(p, i):
#         print(i)

# p = r"[A-Z][a-z]"
# for i in a:
#     if re.search(p, i):
#         print(i)
# print(re.search("a.*b$", a))

# c =re.sub(r"[ ,.]", ":", a)
# print(c)
# print(re.match("^ab*", a))

# p = r"ab{2,3}"
# print(re.match("^ab{2,3}", a))

# p = r"[a-z][_]"
# for i in a:
#     if re.search(p, i):
#         print(i)

# r = r"[ ,.]"
# if re.search(r, a):
#     a = re.sub(r, ":", a)
# print(a)
