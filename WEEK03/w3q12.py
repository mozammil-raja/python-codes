from math import sqrt

def isPrime(n):
    for i in range(2, (n//2)+1):
        if (n % i == 0):
            return i, False
    return True
    
num = int(input("Enter a num: "))
if (num<=1): print("Enter Positive Number greater than 1");
else:
    result = isPrime(num)
    if result == True:
        print("the number is prime.")
    else:
        print(f"the number is not a prime. 2nd factor is {result[0]}")
        
        