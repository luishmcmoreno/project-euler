def num_divisors(n):
    if n % 2 == 0: n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors

num = 500
n = 1

num_divisors_n = num_divisors(n)
num_divisors_n_plus_1 = num_divisors(n + 1)

while ((num_divisors_n * num_divisors_n_plus_1) < num):
    n += 1
    num_divisors_n = num_divisors_n_plus_1
    num_divisors_n_plus_1 = num_divisors(n + 1)

print (n * (n + 1))/2