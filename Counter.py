"""
initialize ants = 1

while user does not quit:
    display the number of ants today
    ask the user how many ants they kill (or if they want to quit)
    if user wants to quit:
        exit the loop
    else:
        double the number of ants for each ant killed
    wait for next day

ants = 1
"""

while True:
    print(f"Number of ants today: {ants}")
    user_input = input("How many ants will you kill today? (enter 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        killed_ants = int(user_input)
        ants -= killed_ants  # remove the killed ants
        ants *= 2  # double the remaining ants for the next day
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")

print("Simulation ended.")
