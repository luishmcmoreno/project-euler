def isPrime(n):
    for i in range(n-1, int(n**(0.5)) - 1, -1):
        if i == 1:
            break
        if (n % i == 0):
            return False
    return True

i = 1
num = 3
while i <= 10001:
    if (isPrime(num)):
        i += 1
    num += 2
print num