# pattern_drawing.py

# Step 1: Ask the user for size
size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize row counter
row = 0

# Step 3: Use a while loop for rows
while row < size:
    # Step 4: Use a for loop for columns
    for col in range(size):
        print("*", end="")  # print stars in one line
    print()  # move to next line after finishing a row
    row += 1  # go to next row

