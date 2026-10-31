# The program should begin by displaying the message "How many mountains should I display?".
print("How many mountains should I display?")

# The program should then read the user's.

num_mountains = int(input())

#Finally, the program should use a for loop to display the specified number of ASCII mountains.
for _ in range(num_mountains):
    print("    /\\")
    print("   /  \\")
    print("  /    \\")
    print(" /      \\")
    print("/        \\")
