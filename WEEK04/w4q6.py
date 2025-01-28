def is_perfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return num == sum

num = int(input("Enter a number: "))
if is_perfect(num):
    print(True)
else:
    print(False)