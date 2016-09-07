# Problem 16 

def power(): 
	numb1 = str(2**1000)
	
	sumtotal = 0 
	for i in range (len(numb1)): 
		sumtotal += int(numb1[i])
	print sumtotal

