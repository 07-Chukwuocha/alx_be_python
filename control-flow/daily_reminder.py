# daily_reminder.py

# Step 1: Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task with match-case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Step 3: Add time-sensitivity message
if time_bound == "yes":
    reminder += " That requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Step 4: Output the final reminder
print("Reminder:", reminder)

