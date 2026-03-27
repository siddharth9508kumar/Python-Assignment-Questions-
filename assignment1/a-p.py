# wap toenter two integers from the keybboard and perform a;; the arithematic operations on them
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print("The sum of the two integers is: ", a + b)
print("The difference of the two integers is: ", a - b)
print("The product of the two integers is: ", a * b)
if b != 0:
    print("The quotient of the two integers is: ", a / b)
else:    print("Cannot divide by zero")
print("The modulus of the two integers is: ", a % b)
print("The floor division of the two integers is: ", a // b)
print("The exponentiation of the two integers is: ", a ** b)