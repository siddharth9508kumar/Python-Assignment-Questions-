# WAP to print twin prime numbers between 1 and N
n=int(input("Enter the value of N: "))
for i in range(1,n):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        if i+2<n:
            count=0
            for k in range(1,i+3):
                if (i+2)%k==0:
                    count+=1
            if count==2:
                print(i,"and",i+2,"are twin prime numbers")