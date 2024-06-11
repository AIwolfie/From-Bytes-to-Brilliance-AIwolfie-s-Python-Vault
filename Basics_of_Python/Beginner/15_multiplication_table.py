# Program to display the multiplication table of a given number

# Prompt the user to enter a number
num = int(input("Enter the number for which you want the multiplication table: "))

# Loop through numbers 1 to 10 and print the multiplication table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

