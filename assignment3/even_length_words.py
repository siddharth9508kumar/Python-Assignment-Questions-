# WAP to print even length words in a string
string=input("Enter a string: ")
words=string.split()
print("Even length words in the string are:")
for word in words:
    if len(word)%2==0:
        print(word)