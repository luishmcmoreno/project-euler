serie = 0
for i in range(1, 1001):
  serie += i**i
print serie % (10**10)