# WAP to input two dictionaries and merge them into a single dictionary.
d1=eval(input("Enter the first dictionary: "))
d2=eval(input("Enter the second dictionary: "))
d1.update(d2)
print("Merged dictionary: ",d1)
    