def sq(a,b):
    for i in range(a, b):
        yield i**2
c = sq(5, 19)
for n in c:
    print(n)
