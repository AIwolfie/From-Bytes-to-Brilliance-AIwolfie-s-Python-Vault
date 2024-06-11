num = int(input("Enter the Number: "))

fact = 1

if num < 0:
    print("please enter valid number.")
if num == 0:
    print("factorial of 0 is", 1)
if num > 0:
    for i in range (1, num+1):
        fact = fact * i

print(f"factorial of given number is {fact}")