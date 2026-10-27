# program should start by displaying the message " How many apples should I remove?".
print("How many apples should I remove?")

# the program should then read in the user's response.
apples_to_remove = int(input())
# program should then create a variable to track the number of removed apples and set this to 0.
removed_apples = 0
# the program should then use a while loop to do the fllowing:
while removed_apples < apples_to_remove:
    # display the message "Removing an apple..."
    print("Removing an apple...")
    # increment the number of removed apples by 1.
    removed_apples += 1
# once the while loop is complete, the program should display the message "All done!".
print("All done!")