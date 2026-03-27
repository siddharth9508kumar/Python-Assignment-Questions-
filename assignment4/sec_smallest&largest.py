# WAP to find the second smallest and second largest 
nums=[]
for i in range(5):
    n=int(input("Enter a number: "))
    nums.append(n)
smallest=largest=nums[0]
for num in nums:
    if num<smallest:
        smallest=num
    elif num>largest:
        largest=num
second_smallest=second_largest=None
for num in nums:
    if num!=smallest and (second_smallest is None or num<second_smallest):
        second_smallest=num
    elif num!=largest and (second_largest is None or num>second_largest):
        second_largest=num

print("Second smallest number is:", second_smallest)
print("Second largest number is:", second_largest)