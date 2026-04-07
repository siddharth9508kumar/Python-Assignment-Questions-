# WAP to count the line present in the file...
f=open("myfile.txt","r")
lines=f.readlines()
print("The number of lines in the file is:",len(lines))
f.close()