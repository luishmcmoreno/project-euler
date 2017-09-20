def is_pandigital(a, b):
	prod = a * b
	if (a > b):
		term = str(prod) + str(a) + str(b)
	else:
		term = str(prod) + str(b) + str(a)
	if len(term) != 9: return False
	numbers = []
	for i in term:
		if (i in numbers): return False
		if (i == '0'): return False
		numbers.append(i)
	return term

sum = 0
products = []
for i in range(2000):
	for j in range(2000):
		numb = is_pandigital(i, j)
		product = i * j
		if numb and not product in products:
			products.append(product)
			sum += product
print sum
