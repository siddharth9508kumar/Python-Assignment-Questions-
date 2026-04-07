# WAP to write the file line by line...
f=open("myfile.txt","w")
lines=f.readlines()
for line in lines:
    f.write(line)
f.close()