"""Program to check if a number is prime or not"""

number = 29
is_prime = True  # Assume it's prime until proven otherwise

if number <= 1:
    is_prime = False
else:
    # Check factors up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

# Output result
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
