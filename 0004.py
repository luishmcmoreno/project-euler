a1 = 999
a2 = 999

def is_palindrome(numb):
	numb = str(numb)
	reverse_numb = numb[::-1]
	return numb == reverse_numb

i = 0

product = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		current_prod = i * j
		if is_palindrome(current_prod):
			if current_prod > product:
				product = current_prod 
print product