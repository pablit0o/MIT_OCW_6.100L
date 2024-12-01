## 6.100A PSet 1: Part B
## Name: Pablo Silva
## Time Spent: 00:11:06
## Collaborators: N/A

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################

yearly_salary = float(input('Enter your yearly salary: '))
portion_saved = float(input('Enter the portion of your salary to save, as a decimal: '))
cost_of_dream_house = float(input('Enter the cost of your dream house: '))
portion_down_payment = 0.25 * cost_of_dream_house
semi_annual_raise = float(input('Enter your semi annual raise, as a decimal: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################

# Initializing the monthly salary makes it more convenient to calculate the number of months. - Pablo Silva
monthly_salary = yearly_salary / 12
amount_saved = 0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################

# This conditional statement ONLY works if your saved amount hasn't surpassed the cost of the house. - Pablo Silva
while (amount_saved < portion_down_payment):
    # Writting += achieves the same value as amount_saved == amount saved + x. - Pablo Silva
    amount_saved += (portion_saved * monthly_salary + (amount_saved * (r / 12)))
    # It is essential that you include the first part of the conditional statement, otherwise the monthly salary will increase by the first month. - Pablo Silva
    # The % symbol represents modulo, which checks if the remainder of months divided by six is equal to zero. - Pablo Silva
    if months != 0 and months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
    # Make sure to increment your variable for every time it adds onto the amount saved. - Pablo Silva
    months += 1
    
print('Number of months: ', months)