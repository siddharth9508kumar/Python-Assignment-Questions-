#WAP to enter s string and print it in reverse order and also count the number of vowels and consonants in the string
str=input("Enter a string: ")
vowels=0
consonants=0
print("The reverse of the string is: ", end="")
for i in range(len(str)-1, -1, -1):
    print(str[i], end="")
    if str[i].lower() in "aeiou":
        vowels += 1
    elif str[i].isalpha():
        consonants += 1
print("\nThe number of vowels in the string is: ", vowels)
print("The number of consonants in the string is: ", consonants)