# Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you, {name}!")

email = input("What is your email address? ")
print(f"Thank you for providing your email address, {name }")

phone_number = input("Enter your phone number: ")
print(f"Thank you for providing your phone number, {name }")

Dob= input("Enter your date of birth (DD/MM/YYYY): ")
print(f"Thank you for providing your date of birth, {name }")

# save file in txt file

with open("../data/info.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone Number: {phone_number}\n")
    file.write(f"Date of Birth: {Dob}\n")
