num = int(input("Enter a number: "))
temp = num
Sum = 0
power = len(str(num))

while temp > 0:
    digit = temp % 10
    Sum += digit ** power
    temp //= 10

if num == Sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
