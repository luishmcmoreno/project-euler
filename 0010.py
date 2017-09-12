# NOT FINISHED, TOO SLOW

def isPrime(n):
	initial = int(n**(0.5));
	if initial % 2 == 0:
		if n % initial == 0:
			return False
		initial -= 1
	for i in range(initial, n, 2):
		if i == 1:
			break
		if (n % i == 0):
			return False
	return True

num = 3
sum = 2
while num < 2000000:
	if (isPrime(num)):
		sum += num
	num += 2
	if (num%1001 == 0): 
		print num 
print sum