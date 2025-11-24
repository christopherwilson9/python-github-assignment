python_github_assignment
#Welcome message
print("Welcome to my Python assignment!")

#User Input
hours = input("How many hours did you study today? ")

#Input Data
hours = float(hours)
expect ValueError:
    print("Please enter a valid number.")
    exit()
weekly_hours = hours * 8

#Final Message
print(f"You are on track to study {weekly_hours} hours this week.")
