from math import sqrt, floor
numb = 600851475143
current = int(floor(sqrt(numb)))

def is_prime(a):
	return all(a % i for i in xrange(2, a))

def nextFactor(numb, current):
	current -= 1
	while (numb % current != 0):
		current -= 1
	return current

current = nextFactor(numb, current)
while (not is_prime(current)):
	current = nextFactor(numb, current)

print current
