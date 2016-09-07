# Problem 20 

def fact():
	number = 1 
	numberhold = 0
	for i in range (1, 101):
		number = number * i 
	ranged = len(str(number))
	for i in range (ranged): 
		numberhold += int(str(number)[i])
	print numberhold

fact()
