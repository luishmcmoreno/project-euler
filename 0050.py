from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

def mark_multiples(arr, n):
    i = n*2
    while i < len(arr):
        arr[i] = False 
        i += n

n = 1000000
sieve = [True] * n 
sieve[0] = False
sieve[1] = False
i = 2
while (i <= int(n**(0.5))):
    mark_multiples(sieve, i)
    i += 1
    while (not sieve[i]): i += 1

primes = []
prime_sum = []

i = 0
for numb in sieve:
    if (numb):
        primes.append(i)
    i += 1

j = 1
prime_sum.append(0)
for prime in primes:
    prime_sum.append(prime_sum[j-1] + primes[j -1])
    j += 1
i = 0
number_of_primes = 0
for sum in prime_sum:
    for j in range(i - number_of_primes + 1, -1, -1):
        if (prime_sum[i] - prime_sum[j] > n): break
        if (binary_search(primes, prime_sum[i] - prime_sum[j]) >= 0):
            number_of_primes = i - j
            result = prime_sum[i] - prime_sum[j]
    i += 1
print result