def f_p(a):
    d = []
    s = True
    for i in range(0,len(a)-1):
        for j in range(2,a[i]):
            if a[i]%j != 0:
                s = False  
        if(s):
            d.append(a[i])      
    return d
r = f_p([1, 2, 3, 9, 7, 10,11, 13])
print(r)
