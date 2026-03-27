# WAP to print all the prime factors of the number
num = int(input("Enter a  three digit number: "))
print("The prime factors of the number are: ", end="")
for i in range(2, num):
    while num % i == 0:
        print(i, end="  ")
        num = num // i
