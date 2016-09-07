# Problem 50 

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def consprime (): 
	largestsofar = [0,0]
	numb = 0
	mult = 0
	while numb < 1000001:
		hold = 0
		count = 0
		if isprime(numb): 
			for i in range (1, numb): 
				
				if isprime(i): 
					hold += i
					count += 1
				if numb == hold: 
					if largestsofar[0] < count: 
						largestsofar = [count, i]
		mult += 1
		numb = 2*mult + 1

		print numb
	print largestsofar 
consprime()

