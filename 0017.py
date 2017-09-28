units = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
decimals = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
thounsand = 11

sum = 0
for i in range(1, 1000):
  decimal = i % 100
  unit = decimal % 10
  hund = i / 100
  if (hund):
    sum += hundred + units[hund]
    if (decimal != 0):
      sum += 3
  if (decimal < 20):
    sum += units[decimal]
  else:
    sum += units[unit] + decimals[decimal/10]
sum += thounsand
print sum