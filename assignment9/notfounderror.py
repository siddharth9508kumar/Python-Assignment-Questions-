# WAP to handle file not found error
try:
    f=open("non_existent_file.txt", "r")
    content=f.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")

