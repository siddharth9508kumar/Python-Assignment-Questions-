# WAP to convert all the characters in a given string to uppercase and lowercase using map function.
def swap(y):
    if y.isupper():
        return y.lower()
    else:
        return y.upper()
x=input("Enter the string: ")
list1=list(map(swap,x))
print("The string with swapped cases is: ", ''.join(list1))