# WAP to use finally block to demonstrate its execution regardless of exceptions
try:
    f=open("sample.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed")