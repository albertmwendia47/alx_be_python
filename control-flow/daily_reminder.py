
Task = input("Enter your task: ")
Time_bound= input("Is the task time-bound? (yes or no): ").lower()
Priority = input("Enter the task priority (high, medium, low): ").lower()

match Priority:
    case "high":
        reminder = f"Task '{Task}' has high priority"
    case "medium":
        reminder = f"Task '{Task}' has medium priority"
    case "low":
        reminder = f"Task '{Task}' has low priority"
    case _:
        reminder = f"Task '{Task}' has an unknown priority"

if Time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
