power_of_2 = lambda x: x ** 2

numbers = range(10)

powers_of_2 = map(power_of_2, numbers)

print(list(powers_of_2))
