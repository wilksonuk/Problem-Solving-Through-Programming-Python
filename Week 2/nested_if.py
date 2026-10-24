# Prompt the user for the cover type of the book
print("What type of cover does the book have?")
cover_type = input()

# Check if the cover type is soft
if cover_type == "soft":
    # Prompt the user to check if the book is perfect-bound
    print("Is the book perfect-bound?")
    perfect_bound = input()
    
    # Nested check for perfect bound
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")

# Check if the cover type is hard
elif cover_type == "hard":
    print("Books with hard covers can be more expensive!")

