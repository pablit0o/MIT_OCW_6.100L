## 6.100A PSet 1: Part B
## Name: Pablo Silva
## Time Spent: 00:05:27
## Collaborators: N/A

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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
