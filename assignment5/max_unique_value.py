# WAP to create dictionary and print the key with maximum unique value.
d=eval(input("Enter the dictionary: "))
max_key=max(d,key=d.get)
print("Key with maximum unique value: ",max_key)