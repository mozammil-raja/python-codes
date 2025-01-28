str = input("Enter a sentence: ")
dict = {}

for s in str:
    if s in dict: dict[s] += 1
    else: dict[s] = 1

print(dict)