def fibonacci(n):
    fib_list = [0, 1]
    for _ in range(n - 2):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

n = int(input("Enter number of Fibonacci numbers to generate: "))
print(fibonacci(n))
