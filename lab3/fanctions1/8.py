def s_g(a):
    c = [0, 0, 7, 'x']
    for i in range(len(a)):
        if a[i] == c[0]:
            c.pop(0)
    return len(c)==1
r = s_g([1, 2, 3, 8])
print(r)

 
