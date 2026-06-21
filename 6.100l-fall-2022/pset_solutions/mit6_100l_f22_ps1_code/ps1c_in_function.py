def part_c(initial_deposit):
	#########################################################################
	house_cost = 800000
	down_payment = house_cost * 0.25 # use less code
	months = 36
	epsilon = 100
	steps = 0
	
	# Bisection jargon
	high = 1.0
	low = 0.0
	r = (high + low) / 2
	
	amount_saved = initial_deposit * pow(1 + (r/12), months)
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	# Edge case 1
	if (initial_deposit >= down_payment - epsilon):
	    epsilon = 100000000000 # Arbitrarily long number to skip bisection search
	    r = 0.0
	
	# Epsilon is exclusive (not >)
	while (abs(amount_saved - down_payment) >= epsilon):
	    steps += 1
	    if (amount_saved < down_payment):
	        low = r
	    else:
	        high = r
	    
	    r = (low + high) / 2
	    amount_saved = initial_deposit * pow(1 + (r/12), months)
	
	    # Edge case #2 -> no return rate good enough for 3 years
	    if (steps >= 36):
	        r = None
	        break
	
	print(f"Best savings rate: {r}")
	print(f"Steps in bisection search: {steps}")
	return r, steps