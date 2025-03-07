a = input("Enter ")
b = 0
c = 0
for i in range( len(a)):
    if a[i].isupper():
        b+=1
    else:
        c+=1
print(b, c)