def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i != 0:
            continue
        else:
            return False
    return True

def print_prime_numbers(start, end):
    """Print all prime numbers in the given interval."""
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

if __name__ == "__main__":
    start = int(input("Enter the start of the interval: "))
    end = int(input("Enter the end of the interval: "))
    print(f"Prime numbers between {start} and {end} are:")
    print_prime_numbers(start, end)
