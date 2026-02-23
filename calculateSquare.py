# Program to calculate squares of numbers and summarize

numbers = [2, 4, 6, 8, 10]

# Using a for loop to calculate squares
squares = []
for num in numbers:
    squares.append(num ** 2)

print("Number | Square")
print("---------------")
for i in range(len(numbers)):  # Another loop for display
    print(f"{numbers[i]}      | {squares[i]}")

# Using a while loop to calculate sum of squares
i = 0
total = 0
while i < len(squares):
    total += squares[i]
    i += 1

print(f"\nTotal of squares: {total}")
