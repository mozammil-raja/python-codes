str = input("Enter a string: ")

up_case_count = 0
low_case_count = 0

for c in str:
    if c.isupper():
        up_case_count += 1
    if c.islower():
        low_case_count += 1

print(f"uppercase count = {up_case_count}, lowercase count = {low_case_count}")