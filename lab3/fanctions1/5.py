from itertools import permutations

def p(s):
    r = permutations(s)
    for i in r:
        print(*i)

s = input()
r= p(s)
