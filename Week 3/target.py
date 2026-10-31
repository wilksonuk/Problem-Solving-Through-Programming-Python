# The program should begin by displaying the message "How far are we from the target?".
print("How far are we from the target?")

# The program should then read in the user's response (number of steps).

num_steps = int(input())

# Finally, the program should use a for loop to display the number of steps remaining.

for _ in range(num_steps):
    print(f" {num_steps - _} steps remaining...")
