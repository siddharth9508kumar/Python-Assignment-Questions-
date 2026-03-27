# WAP to enter time in minutes and print it in hours and minutes
time_m = int(input("Enter the time in minutes: "))
time_h = time_m // 60
time_m = time_m % 60
print("The time in hours and minutes is: ", time_h, "hours and", time_m, "minutes")