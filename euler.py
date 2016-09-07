import random 
import math 
import time
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


# Question 5 - Smallest Number to be divisible by all number from 1-20

def smallest_multiple ():
	not_found = True
	i = 1
	while not_found: 
		i += 1 
		if i % 2 == 0: 
			if i % 3 == 0: 
				if i % 4 == 0: 
					if i % 5 == 0: 
						if i % 6 == 0: 
							if i % 7 == 0: 
								if i % 8 == 0: 
									if i % 9 == 0: 
										if i % 10 == 0: 
											if i % 11 == 0: 
												if i % 12 == 0: 
													if i % 13 == 0: 
														if i % 14 ==0:
															if i % 15 ==0: 
																if i % 16 == 0:
																	if i % 17 == 0:
																	 	if i % 18 ==0:
																	 		if i % 19 == 0: 
																	 			if i % 20 == 0: 
																	 				not_found = False 
																	 				print i 





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




# Question 8 - Largest Product in a Series

def largestprod (): 
	number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
	largest_so_far = 0
	for i in range (1, 988): 
		numbers = number[0+i: 13+i]
		
		product = 1
		for i in range (13): 
			product = product * int(numbers[i])
		if largest_so_far < product: 
			largest_so_far = product
	print largest_so_far


# Question 10 - Summation of primes


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

def sumprime (): 
	sum = 0 
	i = 2
	count = 1
	while i < 2000000:
		if isprime(i):
			sum += i

		i = 2*(count) + 1
		count += 1
	print sum


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


	 		

# Question 11 - Largest product in a grid 

def left_right (): 
	numbers = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
	numberarray = numbers.split() 
	largestprod = 0
	for i in range (101):
		prodhold = 1
		for pos in range(5):
			if numberarray[i+pos][0] == "0": 
				prodhold = prodhold * int(numberarray[i+pos][1])
			else: 
				prodhold = prodhold * int(numberarray[i+pos])
		if largestprod < prodhold: 
			largestprod = prodhold
	print largestprod


def up_down (): 
	numbers = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
	numberarray = numbers.split() 
	largestprod = 0 
	move = 0 
	while move < 20: 
		for i in range(1,6): 
			prodhold = 1
			for val in range(5): 
				if numberarray[val+(20*i)+move][0] == "0": 
					prodhold = prodhold * int(numberarray[val+(20*i)+move][1])
				else: 
					prodhold = prodhold * int(numberarray[val+(20*i)+move])
			if largestprod < prodhold: 
				largestprod = prodhold
		move += 1 
	print largestprod


def diag(): 
	numbers = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"
	numberarray = numbers.split() 
	largestprod = 0 






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





# Problem 16 

def power(): 
	numb1 = str(2**1000)
	
	sumtotal = 0 
	for i in range (len(numb1)): 
		sumtotal += int(numb1[i])
	print sumtotal



#Problem 13 

def tendig(): 
	sumhold = 0 
	numb = "37107287533902102798797998220837590246510135740250463769376774900097126481248969700780504170182605387432498619952474105947423330951305812372661730962991942213363574161572522430563301811072406154908250230675882075393461711719803104210475137780632466768926167069662363382013637841838368417873436172675728112879812849979408065481931592621691275889832738442742289174325203219235894228767964876702721893184745144573600130643909116721685684458871160315327670386486105843025439939619828917593665686757934951621764571418565606295021572231965867550793241933316490635246274190492910143244581382266334794475817892575867718337217661963751590579239728245598838407582035653253593990084026335689488301894586282278288018119938482628201427819413994056758715117009439035398664372827112653829987240784473053190104293586865155060062958648615320752733719591914205172558297169388870771546649911559348760353292171497005693854370070576826684624621495650076471787294438377604532826541087568284431911906346940378552177792951453612327252500029607107508256381565671088525835072145876576172410976447339110607218265236877223636045174237069058518606604482076212098132878607339694128114266041808683061932846081119106155694051268969251934325451728388641918047049293215058642563049483624672216484350762017279180399446930047329563406911573244438690812579451408905770622942919710792820955037687525678773091862540744969844508330393682126183363848253301546861961243487676812975343759465158038628759287849020152168555482871720121925776695478182833757993103614740356856449095527097864797581167263201004368978425535399209318374414978068609844840309812907779179908821879532736447567559084803087086987551392711854517078544161852424320693150332599594068957565367821070749269665376763262354472106979395067965269474259770973916669376304263398708541052684708299085211399427365734116182760315001271653786073615010808570091499395125570281987460043753582903531743471732693212357815498262974255273730794953759765105305946966067683156574377167401875275889028025717332296191766687138199318110487701902712526768027607800301367868099252546340106163286652636270218540497705585629946580636237993140746255962240744869082311749777923654662572469233228109171419143028819710328859780666976089293863828502533340334413065578016127815921815005561868836468420090470230530811728164304876237919698424872550366387845831148769693215490281042402013833512446218144177347063783299490636259666498587618221225225512486764533677201869716985443124195724099139590089523100588229554825530026352078153229679624948164195386821877476085327132285723110424803456124867697064507995236377742425354112916842768655389262050249103265729672370191327572567528565324825826546309220705859652229798860272258331913126375147341994889534765745501184957014548792889848568277260777137214037988797153829820378303147352772158034814451349137322665138134829543829199918180278916522431027392251122869539409579530664052326325380441000596549391598795936352974615218550237130764225512118369380358038858490341698116222072977186158236678424689157993532961922624679571944012690438771072750481023908955235974572318970677254791506150550495392297953090112996751986188088225875314529584099251203829009407770775672113067397083047244838165338735023408456470580773088295917476714036319800818712901187549131054712658197623331044818386269515456334926366572897563400500428462801835170705278318394258821455212272512503275512160354698120058176216521282765275169129689778932238195734329339946437501907836945765883352399886755061649651847751807381688378610915273579297013376217784275219262340194239963916804498399317331273132924185707147349566916674687634660915035914677504995186714302352196288948901024233251169136196266227326746080059154747183079839286853520694694454072476841822524674417161514036427982273348055556214818971426179103425986472045168939894221798260880768528778364618279934631376775430780936333301898264209010848802521674670883215120185883543223812876952786713296124747824645386369930090493103636197638780396218407357239979422340623539380833965132740801111666627891981488087797941876876144230030984490851411606618262936828367647447792391803351109890697907148578694408955299065364044742557608365997664579509666024396409905389607120198219976047599490197230297649139826800329731560371200413779037855660850892521673093931987275027546890690370753941304265231501194809377245048795150954100921645863754710598436791786391670211874924319957006419179697775990283006991536871371193661495281130587638027841075444973307840789923115535562561142322423255033685442488917353448899115014406480203690680639606723221932041495354150312888033953605329934036800697771065056663195481234880673210146739058568557934581403627822703280826165707739483275922328459417065250945123252306082291880205877731971983945018088807242966198081119777158542502016545090413245809786882778948721859617721078384350691861554356628840622574736922845095162084960398013400172393067166682355524525280460972253503534226472524250874054075591789781264330331690"
	for i in range (100):
		sumhold += int(numb[i*50:(i+1)*50])
	print str(sumhold)[0:10]

tendig()


	

#Problem 12 





def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s
 
def amicable_pairs_xrange(low,high):
    L = [sum_divisors(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs
 
def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])
ans = sum_pairs(amicable_pairs_xrange(1,10000))
print ans




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




