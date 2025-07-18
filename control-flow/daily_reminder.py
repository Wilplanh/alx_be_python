# daily_reminder.py

print("=== Daily Task Reminder ===")

# Prompt user for task
task = input("Enter your task: ").strip()

# Prompt user for priority with validation
while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter high, medium, or low.")

# Prompt for time sensitivity with validation
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ["yes", "no"]:
        break
    print("Invalid response. Please enter yes or no.")

# Match case on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"

# Add time-bound message
if time_bound == "yes":
    reminder += " is a high priority task that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Output final reminder
print("\nReminder:", reminder)
    