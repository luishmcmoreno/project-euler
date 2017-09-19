def sum_of_fifth_power_digits(n):
	sum = 0
	while (n > 0):
		d = n % 10
		n /= 10
		sum += d**5
	return sum

sum = 0
for i in range(2, 355000):
	if i == sum_of_fifth_power_digits(i):
		sum += i
print sum
