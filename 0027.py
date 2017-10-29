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


def is_prime(n):
    return sieve[n]

def quadratic_formula(n, a, b):
    return n**2 + a*n + b

a_max = -1
b_max = -1
n_max = -1

for a in range(-999, 1001, 2):
    for b in range(-1001, 1001):
        if (not is_prime(b)): continue
        n = 0
        while (is_prime(quadratic_formula(n, a, b))):
            n += 1
        if (n > n_max):
            a_max = a
            b_max = b
            n_max = n

print a_max*b_max