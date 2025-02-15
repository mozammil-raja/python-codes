def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_series(n):
    if n <= 0:
        print("Invild input (number<=0)")
        return
    print("Fibonacci Series:", end=" ")
    for i in range(1, n + 1):
        print(fibonacci(i), end=", " if i < n else "\n")

n = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_series(n)