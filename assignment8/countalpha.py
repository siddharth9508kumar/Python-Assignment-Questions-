# WAP to count the alphabets present in the file...
f=open("myfile.txt","r")
text=f.read()
alpha=0
for char in text:
    if char.isalpha():
        alpha+=1
print("The number of alphabets in the file is:",alpha)
f.close()