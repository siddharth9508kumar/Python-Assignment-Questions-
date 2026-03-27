# WAP to convert a given list of integer and tuple of integers to string using map function.
def convert(c):
    if c==1:
        return"one"
    elif c==2:
        return"two"
    elif c==3:
        return"three"
    elif c==4:
        return"four"
    elif c==5:
        return"five"
    elif c==6:
        return"six"
    elif c==7:
        return"seven"
    elif c==8:
        return"eight"
    elif c==9:
        return"nine"
    elif c==0:
        return"zero"
    else:
        return"not a number"
list1=eval(input("Enter the list of integers: "))
l2=list(map(convert,list1))
print(l2)
l3=eval(input("Enter the tuple of integers: "))
l4=tuple(map(convert,l3))
print(l4)