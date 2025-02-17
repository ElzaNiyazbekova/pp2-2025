def fun(a):
    for i in range(a+1):
        if i%4==0 and i%3==0:
            yield i
c = fun(45)
for n in c:
    print(n)