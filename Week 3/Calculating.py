# The program should start by displaying the message "Calculating the sum of the first 100 numbers...".
print("Calculating the sum of the first 100 numbers...")

# The program should then use a while loop to calculate the sum of the first 100 numbers from 1 to 100 (inclusive).
i = 1
total = 0
while i <= 100:
    total += i
    i += 1
# Finally, the program should display the message "...Done! The answer is" followed by the answer.
print(f"...Done! The answer is {total}.")
