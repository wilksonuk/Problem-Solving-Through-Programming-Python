# Display start message
print("Program Started!")

# Prompt user for a character and read the response
print("Please enter a standard character:")
letter = input()

# Check if a single character was entered
if len(letter) == 1:
    # Determine the ASCII code using ord()
    value = ord(letter)
    print(f"The ASCII code for {letter} is {value}.")
else:
    # Error message if the length is not 1
    print("Error: You must enter exactly one character.")

# Display end message
print("Program Ended!")

