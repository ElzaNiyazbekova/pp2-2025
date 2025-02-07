def f_33(a):
    d = True
    for i in range(0, len(a)-1):
        if (a[i] == a[i+1] or a[i]==a[i-1]) and a[i]==3:
            d = True
        else:
            d = False
    return d
r = f_33([3, 1, 3])
print(r)