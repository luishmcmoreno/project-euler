
def mark_multiples(arr, n):
    i = n*2
    while i < len(arr):
        arr[i] = False 
        i += n

n = 2000000
sieve = [True] * n 
sieve[0] = False
sieve[1] = False
i = 2
while (i <= int(n**(0.5))):
    mark_multiples(sieve, i)
    i += 1
    while (not sieve[i]): i += 1

i = 0
prime_sum = 0
for numb in sieve:
    if (numb):
        prime_sum += i
    i += 1
print prime_sum