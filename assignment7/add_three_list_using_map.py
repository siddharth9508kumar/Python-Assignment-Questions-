# WAP to add three given lists usiong map function and lambda function.
list1=eval(input("Enter the first list of integers: "))
list2=eval(input("Enter the second list of integers: "))
list3=eval(input("Enter the third list of integers: "))
added_list=list(map(lambda x,y,z: x+y+z, list1, list2, list3))
print("The added list is: ", added_list)