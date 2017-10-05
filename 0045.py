import math
def is_pentagonal(n):
  pent = (math.sqrt(1 + 24 * n) + 1) / 6
  return pent == int(pent)

def hexagonal(n):
  return n*(2*n - 1)

h = 144

while (not is_pentagonal(hexagonal(h))):
  h += 1

print hexagonal(h)