num = int(input("Enter a Number: "))

if num < 0:
    print("please enter positive number: ")
else:
    sum = 0
    while num>0:
        sum += num
        num -= 1
    print(sum)