# multiplication_table.py

# Step 1: Prompt user for input
number = int(input("Enter a number to see its multiplication table: "))

# Step 2: Use a for loop to generate multiplication table from 1 to 10
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
