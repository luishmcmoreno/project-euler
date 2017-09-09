a1 = 1
a2 = 2
sum = 0
index = 3
limit = 10**999
while a2 < limit:
	nextTerm = a2 + a1
	a1 = a2
	a2 = nextTerm
	index += 1
print index
