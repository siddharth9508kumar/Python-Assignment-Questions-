# WAP to print Fibonacci series (first 15 terms,without recurssion)
def fibonacci():
    a, b = 0, 1
    for _ in range(15):
        print(a, end=' ')
        a, b = b, a + b
fibonacci()
