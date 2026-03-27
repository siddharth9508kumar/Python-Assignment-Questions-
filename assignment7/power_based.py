# WAP to create a list containing the power of said number in base.
import math
x=eval(input("Enter the power list: "))
y=eval(input("Enter the number list: "))
def power(x,y):
    z=math.pow(y,x)
    return z
list1=list(map(power,x,y))
print("The power list is: ", list1)