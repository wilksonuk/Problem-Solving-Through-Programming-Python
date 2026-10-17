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

# Define the project folder
project_folder = Path(__file__).parent.parent

# Create the data folder if it does not exist
data_folder = project_folder / "data"
data_folder.mkdir(parents=True, exist_ok=True)

# Define the file path
file_path = data_folder / "info.txt"

# Save the information
with open(file_path, "w", encoding="utf-8") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Phone Number: {phone_number}\n")
    file.write(f"Date of Birth: {dob}\n")

print(f"\nInformation saved successfully in: {file_path}")
