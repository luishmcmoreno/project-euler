import math

limit = 20

x = (limit * 2)
y = limit

a = math.factorial(x)
b = math.factorial(y)
c = math.factorial(x - y)
div = a // (b * c)

print div