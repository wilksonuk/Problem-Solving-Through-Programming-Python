# The function should do the following:
# Display the message "Crossed step" for each step crossed
# If the distance is more than 5 then the message "The bridge is collapsing!" should be displayed.
# Otherwise the message "we must keep going!" should be displayed.
# Finally, the program should contain the following calls to your cross_bridge function:

# cross_bridge(3)
# cross_bridge(6)
def cross_bridge(distance):
    for step in range(distance):
        print("Crossed step")
    if distance > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")
    
cross_bridge(3)
cross_bridge(6)