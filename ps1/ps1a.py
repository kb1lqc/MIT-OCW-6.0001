#Declare initial values
current_savings = 0
r = 0.04
total_months = 0

#Get input from user
annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter  the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

#Calculate down payment
portion_down_payment = total_cost * 0.25

#Iterate through each month adding savings and compounding interest
while current_savings < portion_down_payment:
    # Increase month count
    total_months += 1

    current_savings += (current_savings * r + annual_salary * portion_saved) / 12

#Print total months needed to save down payment
print("Number of moths:", total_months)