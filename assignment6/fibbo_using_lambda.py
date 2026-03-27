# WAP to print fibbonacci series using lambda function.
n=int(input("Enter the number of terms: "))
fib=lambda n: n if n<=1 else fib(n-1)+fib(n-2)
print("Fibbonacci series: ")
for i in range(n):
    print(fib(i), end=" ")