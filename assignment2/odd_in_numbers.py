# WAP to enter a 5 digit number and print all the odd digits in the number
num = int(input("Enter a 5 digit number: "))
print("The odd digits in the number are: ", end="")
while num > 0:
    digit = num % 10
    if digit % 2 != 0:
        print(digit, end="  ")
    num = num // 10
    