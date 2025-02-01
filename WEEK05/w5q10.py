str = input("Enter a string: ")

count = 0
for x in str:
    if x in "aeiouAEIOU":
        count += 1

print(f"vowel count = {count}")