def fun(a):
    for i in range(a):
        yield i**2
ctr = fun(5)
for n in ctr:
    print(n)