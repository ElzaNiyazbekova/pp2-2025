def fun(a):
    for i in range(a):
        if(i%2!=0):
            yield i
c = fun(23)
for n in c:
    print(n)