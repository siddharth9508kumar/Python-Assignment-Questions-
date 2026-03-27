# WAP to return even num,bers from a list
def return_even_numbers(lst):
    even_numbers = []
    for num in lst:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
# Example usage
numbers = []
for i in range(10):
    n = int(input("Enter a number: "))
    numbers.append(n)
even_numbers = return_even_numbers(numbers)
print("Even numbers in the list:", even_numbers)