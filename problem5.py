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

