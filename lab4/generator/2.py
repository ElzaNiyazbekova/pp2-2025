# def fun(a):
#     for i in range(a):
#         if(i%2!=0):
#             yield i
# c = fun(23)
# for n in c:
#     print(n)

def fun(a):
    for i in range(len(a)):
        a[i].upper()
        if i%3==0:
            yield '\n'+a[i]
        yield a
c = fun('dyhxjxk')
for n in c:
    print(n)