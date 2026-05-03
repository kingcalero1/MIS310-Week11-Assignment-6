# Daily Steps Tracker Program

def main():
    # Function to set the daily steps goal
    def set_steps_goal():
        goal = int(input("Enter your daily steps goal: "))
        return goal

    # Record daily steps for each day of the week
    def record_daily_steps():
        total_steps = 0
        for day in range(1, 8):  # Loop for 7 days
            steps = int(input(f"Enter steps for day {day}: "))
            total_steps += steps  # Add daily steps to total
        return total_steps

    # Function to evaluate weekly performance
    def evaluate_weekly_performance(total_steps, daily_goal):
        average_steps = total_steps / 7  # Calculate average
        print(f"\nYour average daily steps for the week: {average_steps:.2f}")

        # Compare average steps with goal
        if average_steps > daily_goal:
            print("You exceeded your daily steps goal.")
        elif average_steps == daily_goal:
            print("You met your daily steps goal.")
        else:
            print("You did not meet your daily steps goal.")

    # Program flow
    daily_goal = set_steps_goal()
    total_steps = record_daily_steps()
    evaluate_weekly_performance(total_steps, daily_goal)

# Call the main function to run the program
main()