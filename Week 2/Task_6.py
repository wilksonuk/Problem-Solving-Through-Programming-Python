first_num = int(input("Please enter the first number: "))
second_num = int(input("Please enter the second number: "))
third_num = int(input("Please enter the third number: "))

# count up the numbers of even or odd
even_count = 0
odd_count = 0

if first_num % 2 == 0:
    even_count = even_count + 1
else:
    odd_count += 1

if second_num % 2 == 0:
    even_count += 1
else:
    odd_count += 1

if third_num % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")