# We wish to create a fragment of a text adventure game in which the player is exploring a cave. We want to make the program respond to sounds entered by the user.

# Start by creating a new python file custom_functions.py and storing the file in the week4 folder you created previously.

# The program should start by defining a function that has the name listen and which takes 0 parameters.
# The function should do the following:
#     Ask the user to enter a word representing a sound.
#     Display the message "That was a loud" followed by the word entered by user and an exclamation mark.
# Finally, the program should contain a call to your function listen
def listen():
    sound = input("Please enter a word representing a sound: ")
    print(f"That was a loud {sound}!")

listen()