import itertools

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

def rotate(n):
    rotlist = []
    m = str(n)
    counter = 0
    while counter < len(str(n)):
        m = m[1:] + m[0]
        rotlist.append(int(m))
        counter += 1
    return rotlist

def is_circular_prime(n):
    perms = rotate(n)
    for perm in perms:
        if (not sieve[perm]):
            return False;
    return True

num_circular_primes = 0
for i in range(n):
    if (is_circular_prime(i)):
        num_circular_primes += 1
print num_circular_primes