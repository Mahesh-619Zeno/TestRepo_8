import random

target_number = random.randint(1, 10)
guess = 0
while guess != target_number:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Correct!")