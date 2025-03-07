from functools import reduce
from operator import mul
import time
import math
def t(e):
    return all(e)

print(t((True, True, True)))
print(t((True, False, True)))