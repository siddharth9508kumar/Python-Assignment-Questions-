# WAP to enter a temperature in Fahrenheit and convert it to Celsius
temp_f = float(input("Enter the temperature in Fahrenheit: "))
temp_c = (temp_f - 32) * 5 / 9
print("The temperature in Celsius is: ", temp_c)