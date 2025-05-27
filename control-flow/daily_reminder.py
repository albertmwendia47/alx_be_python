
task = input("Enter your task: ")
time_bound= input("Is the task time-bound? (yes or no): ").lower()
priority = input("Enter the task priority (high, medium, low): ").lower()

match priority:
    case "high":
        reminder = f"Task '{task}' has high priority"
    case "medium":
        reminder = f"Task '{task}' has medium priority"
    case "low":
        reminder = f"Task '{task}' has low priority"
    case _:
        reminder = f"Task '{task}' has an unknown priority"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
