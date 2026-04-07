# WAP to divide by zero without handling the exception
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
if b==0:
    print("Cannot divide by zero")
else:
    print("The result is: ",a/b)