# WAP to demonstrate the use of else block in exception handling
try:
    f=open("sample.txt", "r")
except FileNotFoundError:
    print("File not found.")
else:
    print("File opened successfully.")

    f.close()