import math

s = int(input("Enter "))
l = int(input("Enter "))

a = l / (2 * math.tan(math.pi / s))

area = (l * a * s) / 2

print(int(area))