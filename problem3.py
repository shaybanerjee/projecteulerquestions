#Question 3 - Largest Prime Factor 

def is_prime(numbr): 
	largest_prime = 0
	div = 2
	prime = True
	while div < numbr/2 and prime: 
		

		if numbr % div == 0: 
			prime = False
		div += 1
	return prime
	

def largest_p_fac (numb): 
	prime_found = True
	div = 1
	largest_prime = 2
	if is_prime(numb):
		print numb
	else: 
		while prime_found: 
			divi = div + 1 
			div = divi 
			if divi == numb-1: 
				prime_found = False
			elif numb % divi == 0 and is_prime(numb // divi): 
				prime_found = False
				print numb//divi

