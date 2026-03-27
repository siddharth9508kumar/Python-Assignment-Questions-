# WAP to remove duplicate keys from a dictionary and print the resulting dictionary.
d=eval(input("Enter the dictionary: "))
new_d={}
seen_keys=set()
for key, value in d.items():
    if key not in seen_keys:
        new_d[key]=value
        seen_keys.add(key)
print("Dictionary after removing duplicate keys: ",new_d)