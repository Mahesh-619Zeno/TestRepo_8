def add(first_number, second_number): return first_number + second_number
def subtract(first_number, second_number): return first_number - second_number
def multiply(first_number, second_number): return first_number * second_number
def divide(first_number, second_number): return first_number / second_number

print("Select operation: 1.Add 2.Subtract 3.Multiply 4.Divide")
choice = input("Enter choice (1/2/3/4): ")
first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))

if choice == '1':
    print(f"Result: {add(first_num, second_num)}")

elif choice == '2':
    print(f"Result: {subtract(first_num, second_num)}")

elif choice == '3':
    print(f"Result: {multiply(first_num, second_num)}")

elif choice == '4':
    print(f"Result: {divide(first_num, second_num)}")

else:
    print("Invalid input")