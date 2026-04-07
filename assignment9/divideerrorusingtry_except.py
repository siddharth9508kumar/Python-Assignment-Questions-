# WAP to use try-except to handle divide by zero exception
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
try:
    result = a / b
    print("The result is: ", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")