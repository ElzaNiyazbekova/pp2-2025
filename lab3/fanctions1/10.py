def f_u(a):
    a.sort()
    b = []
    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            continue
        else:
            b.append(a[i])
    return b
r = f_u([1, 2, 3, 4, 5, 5, 6, 6, 7])
print(r)