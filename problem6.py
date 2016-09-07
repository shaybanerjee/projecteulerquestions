# Question 6 - Sum Square Difference 


def sumsquares(): 
	value = 0
	for i in range(1, 101):
		value += (i**2)
	return value

def squaresum(): 
	value = 0
	for i in range(1, 101): 
		value += i
	return value ** 2

def difference(): 
	sumofsquares = sumsquares() 
	squareofsums = squaresum() 
	print squareofsums - sumofsquares
	
	

