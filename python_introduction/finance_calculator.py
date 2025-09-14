# finance_calculator.py

# Read user input and convert to float
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a 5% interest rate (simplified model)
annual_savings = monthly_savings * 12
annual_interest_rate = 0.05  # 5%
projected_savings = annual_savings * (1 + annual_interest_rate)

# Output results (formatted to two decimal places)
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

