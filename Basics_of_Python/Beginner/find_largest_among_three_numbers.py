num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
num3 = float(input("Enter third Number: "))

if num1>num2 and num2>num3:
    print(f"{num1} is largest.")
elif num2>num1 and num1>num3:
    print(f"{num2} is largest.")
else:
    print(f"{num3} is largest")