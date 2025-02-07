def r_s(s):
    w = s.split()
    return " ".join(reversed(w))

s = input("Enter ")
r= r_s(s)
print(r)