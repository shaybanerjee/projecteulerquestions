# Question 4 - Largest Palindrome from the product of two 3 digit numbers 

def is_palindrome(num):
	numb = str(num)
	if len(numb) < 2: 
		return True
	else: 
		if numb[0] == numb[-1]:
			return is_palindrome(numb[1:-1])
		else:
			return False

def largest_palindrom ():
	large_pal = 0
	for i in range(100, 1000):
		for num in range(100, 1000): 
			if is_palindrome(i*num):
				if large_pal < i*num:
					large_pal = i*num

	print large_pal

