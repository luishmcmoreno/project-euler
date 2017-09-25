def collatz(n):
  count = 1
  while (n > 1):
    if (n % 2 == 0):
      n = n/2
    else:
      n = 3*n + 1
    count += 1
  return count

limit = 1000001
biggest_count = 0
biggest_starting = 0
for i in range(1, limit):
  current_collatz = collatz(i)
  if current_collatz > biggest_count:
    biggest_count = current_collatz
    biggest_starting = i
print biggest_starting

