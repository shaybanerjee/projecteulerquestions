# Question 7 - 10001st Prime

def is_prime(numbr): 
	largest_prime = 0
	div = 2
	prime = True
	while div < numbr/2 and prime: 
		if numbr == 1: 
			prime = False
		

		elif numbr % div == 0: 
			prime = False
		div += 1
	return prime


def primetarget (): 
	primenumber = 0
	counter = 2
	while primenumber <= 10001: 
		if is_prime (counter):
			prime = counter
			primenumber += 1
		counter += 1
	print prime 

