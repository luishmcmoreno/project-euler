a1 = 1
a2 = 2
sum = 0
while a2 < 4000000:
	if a2 % 2 == 0:
		sum += a2
	nextTerm = a2 + a1
	a1 = a2
	a2 = nextTerm
print sum
