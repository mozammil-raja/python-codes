def SumOfDigit(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num //= 10
    return sum

number = int(input("Enter Number: "))
print(f"Sum of digits of {number} is {SumOfDigit(number)}")
