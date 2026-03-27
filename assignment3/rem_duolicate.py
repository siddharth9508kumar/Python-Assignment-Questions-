# WAP to remove all duplicate elements from a string
string=input("Enter a string: ")
result=""
for char in string:
    if char not in result:
        result+=char
print("String after removing duplicates is:",result)