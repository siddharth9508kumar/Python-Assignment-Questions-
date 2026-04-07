# WAP to hsndle value error ...
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is: ", result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")