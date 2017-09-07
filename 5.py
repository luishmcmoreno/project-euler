def isDivisible(num):
    for i in range(1,21):
        if (num % i <> 0):
            return False
    return True

num = 20
while (not isDivisible(num)):
    num += 20

print num