def fun(a):
    while a>-1:
        yield a
        a -= 1

c = fun(32)
for n in c:
    print(n)