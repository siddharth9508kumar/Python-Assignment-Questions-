#WAP to  triple all numbers in a given list of integers using map function.
list1=eval(input("Enter the list of integers: "))
triple_list=list(map(lambda x: x*3, list1))
print("The triple of the given list is: ", triple_list)