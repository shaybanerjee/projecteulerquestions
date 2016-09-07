# Question 9 - Special Pythagorean triplet (not the best way to do this question)

def spectrip ():
	not_found = True
	while not_found: 
		a = random.randint(0,1000)
		b = random.randint (0, 1000)
	 	c = math.sqrt(a**2 + b**2) 
	 	if a+b+c == 1000: 
	 		not_found = False
	print a*b*c
