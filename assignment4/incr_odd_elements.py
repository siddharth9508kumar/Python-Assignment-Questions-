# WAP to increase odd elements by 5
list1=[]
for i in range(20):
    n=int(input("Enter numbers:"))
    list1.append(n)
for i in range(len(list1)):
    if list1[i]%2!=0:
        list1[i]+=5
print("List after increasing odd elements by 5:", list1)