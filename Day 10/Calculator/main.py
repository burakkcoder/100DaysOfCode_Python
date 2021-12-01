import art

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print(art.logo)

first_number = float(input("What's the first number?: "))
print("+")
print("-")
print("*")
print("/")

while True:
    equals = int()
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    last_number = second_number

    if operation == "+":
        equals = add(first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {equals}")
    elif operation == "-":
        equals = subtract(first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {equals}")
    elif operation == "*":
        equals = multiply(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {equals}")
    elif operation == "/":
        equals = divide(first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {equals}")
    else:
        print("Please type your operation right.")
        continue

    y_n = input(f"Type 'y' to continue calculating with {equals}, or type 'n' to start a new calculation: ")
    if y_n == "n":
        print("Bye")
        break
    elif y_n == "y":
        first_number = equals
        continue

