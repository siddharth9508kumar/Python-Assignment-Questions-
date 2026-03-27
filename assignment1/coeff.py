# WAP to enter the coefficients of a quadratic equation and find the roots of the equation
import math
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
d = b**2 - 4*a*c
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots of the equation are: ", root1, "and", root2)
elif d == 0:
    root = -b / (2*a)
    print("The root of the equation is: ", root)
else:
    print("The equation has no real roots.")