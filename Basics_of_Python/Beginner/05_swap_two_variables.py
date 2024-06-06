# Program to swap two variables

# =>method 1
# Input: Define two variables
a = 2
b = 3

# Print initial values
print("Before swapping: ")
print("a =", a)
print("b =", b)

# Swap using a temporary variable
temp = a
a = b
b = temp

# Print swapped values
print("\nAfter swapping using a temporary variable:")
print("a =", a)
print("b =", b)


# =>method 2
# Input: Define two variables
a = 2
b = 3

# Print initial values
print("Before swapping: ")
print("a =", a)
print("b =", b)

# Swap using tuple unpacking
a, b = b, a

# Print swapped values
print("\nAfter swapping using a tuple unpacking:")
print("a =", a)
print("b =", b)
