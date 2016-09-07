# Problem 14 

def collatz(): 
	largestsofar = [0,0]
	for i in range (1, 1000000):
		num = i
		steps = 0 
		while num != 1: 
			if num % 2 == 0: 
				num = num/2
			else: 
				num = 3*num+1 
			steps += 1 
		if steps > largestsofar[0]: 
			largestsofar = [steps, i]
	print largestsofar[1]



