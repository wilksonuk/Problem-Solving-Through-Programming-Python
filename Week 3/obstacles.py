print("How many obstacles must I avoid?")

obstacles_to_avoid = int(input())
#program should then create a variable to track the number of avoided obstacles and set this to 0.
avoided_obstacles = 0
#program should then use a while loop to do the following:
while avoided_obstacles < obstacles_to_avoid:
    #display the message "Avoiding an obstacle..."
    print("Avoiding an obstacle...")
    #increment the number of avoided obstacles by 1.
    avoided_obstacles += 1
#once the while loop is complete, the program should display the message "Done [n] obstacles avoided!".
print(f"Done {avoided_obstacles} obstacles avoided!")
#finally, the program should display the message "All obstacles have been avoided!".
print("All obstacles have been avoided!")
