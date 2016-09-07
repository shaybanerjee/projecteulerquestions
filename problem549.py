# Question 549 

def smallfact(numb): 
	not_found = True
	m = 1
	while not_found:
		hold = 1
		for i in range (1, m+1): 
			hold *= i 
		if hold % numb == 0: 
			not_found = False
		else: 
			m +=1 
			print m
	print m

smallfact(10**8)



