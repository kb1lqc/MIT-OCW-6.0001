# Declare initial variables
epsilon = 0.01
low = 0
high = 10000
current_savings = 0
r = 0.04
total_months = 36
months = 0
total_cost = 1000000
semi_annual_raise = 0.07
steps = 0

#Get input from user
annual_salary_init = int(input("Enter the starting salary: "))

#Calculate down payment
portion_down_payment = total_cost * 0.25

#calculate bisectional search
""" 
Generate guess of saving rate 1/2 range
iterate over 36 months
compare to downpayment within $100 (10000 * epsilon)
if savings more than downpayment, set guess to high
if savings less than downpayment, set guess to low
repeat until comparison complete
 """
while abs(current_savings - portion_down_payment) >= 10000 * epsilon:
    # Reset current savings to zero
    current_savings = 0

    # Reset annual salary
    annual_salary = annual_salary_init

    #Set initial guess, floor (integer) division
    guess = ((high + low) // 2)

    # run 36 month savings test
    for i in range(total_months):
        if i != 0 and i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
        current_savings += current_savings * (r / 12)
        current_savings += annual_salary / 12 * guess / 10000

    # Check current savings against downpayment, set guess min/max accordingly
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
    
    # Check for infinite loop case, floor (integer) division
    if guess == (high+low)//2:
        break
    
    # Add to step count
    steps += 1

# Check if solution is close enough, else inform no solution
if abs(current_savings - portion_down_payment) <= 10000 * epsilon:
    print("Best savings rate:", guess/10000)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")