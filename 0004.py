a1 = 999
a2 = 999

def is_palindrome(numb):
	numb = str(numb)
	reverse_numb = numb[::-1]
	return numb == reverse_numb

i = 0
while (not is_palindrome(a1 * a2)):
	if (i % 2 == 0):
		a1 -= 1
	else:
		a2 -= 1
	i += 1
print a1, a2, a1*a2