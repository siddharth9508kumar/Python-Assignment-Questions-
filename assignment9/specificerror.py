# WAP to handle a specific exception using try-except block
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("The result is: ", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
finally:
    print("Execution completed")
    