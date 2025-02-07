def p(a):
    b = a[::-1]
    c = False
    for i in range(len(a)):
        if a == b:
            c = True
        else:
            c = False
    if c:
        return("PAlindrom")
    else:
        return("PAlindrom emses")
r = p("123123")
print(r)