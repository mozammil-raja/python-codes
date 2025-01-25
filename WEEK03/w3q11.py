def isFibo(n):
    a, b=0, 1

    while(b<n):
        a, b= b, a+b
    return n==b     


num = (int)(input("Enter Number: "))

if isFibo(num): print(f"{num} is a Fibonacci number ");
else: print(f"{num} is not a Fibonacci number ");