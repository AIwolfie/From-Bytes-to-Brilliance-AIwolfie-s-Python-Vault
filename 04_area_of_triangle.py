# This program calculates the area of a triangle given its base and height
# taking height and base from the user 
height = float(input("Enter the height of triangle: "))
base = float(input("Enter the base of triangle: "))

# find area of triangle
artri = (1/2)*base*height

# display the output
print(f"the area of triangle is {artri}")


# =>method 2 making def function

def calculate_area_of_triangle(height, base):
    return (1/2)*base*height

def main():
    height = float(input("Enter the height of triangle: "))
    base = float(input("Enter the base of triangle: "))

    artri = calculate_area_of_triangle(height, base)

    print(f"the area of triangle is {artri}")

if __name__ == "__main__":
    main()