def is_prime(n):
    for i in range(2, n):
        if (n % i == 0):
            return False
        return True
    
num = int(input("Enter a num: "))
if is_prime(num):
    print(True)
else:
    print(False)