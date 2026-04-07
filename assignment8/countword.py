# WAP to count the number of wrods present in the file...
# add some text in the file before running this code...

f=open("myfile.txt","w")
f.write("This is my first file\n")
f.write("Hello world\n")
f.close()   
f=open("myfile.txt","r")
text=f.read()
words=text.split()
print("The number of words in the file is:",len(words))
f.close()