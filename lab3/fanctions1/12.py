def h(a):
    c = ""
    for i in range(len(a)):       
        for j in range(0, a[i]):  
            c += "*"              
        print(c)                 
        c = ""                    

r = [4, 9, 7]
h(r)