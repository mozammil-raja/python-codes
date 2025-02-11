string = input("Enter a string: ")

if len(string) < 2:
    print("Empty string")
else:
    result = string[:2] + string[-2:]
    print("Modified string:", result)
