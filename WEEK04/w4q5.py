def sum_of_digits(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum += rem
        num //= 10
    return sum

num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")
