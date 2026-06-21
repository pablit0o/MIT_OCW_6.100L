def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05 # Annual rate of return
	
	monthly_salary = yearly_salary / 12
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ## 
	###############################################################################################
	while (amount_saved < cost_of_dream_home * portion_down_payment): # Down payment cost
	    months += 1
	
	    amount_saved += amount_saved * (r/12) # Goes first since its at the "start" of each month
	    amount_saved += (monthly_salary * portion_saved)
	
	    # Month is a multiple of six; do it at the "end" of each month
	    if (months % 6 == 0):
	        yearly_salary += yearly_salary * semi_annual_raise
	        monthly_salary = yearly_salary / 12 # Update the monthly_salary
	
	print(f"Number of months: {months}")
	return months