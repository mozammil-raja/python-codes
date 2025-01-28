def get_fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

num = int(input("Enter a num: "))
print(f"Fact of {num} is {get_fact(num)}")