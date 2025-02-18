data = "Python rules!"

wordList = data.split()
print("list of word:", wordList)

upperCase = data.upper()
print(f"Uppercase of {data}: {upperCase}")

position = data.find("rules")
print("Position of 'rules':", position)

char = input("Enter a character to search: ")
char_pos = data.find(char)
if char_pos != -1:
    print(f"Char - '{char}' at position {char_pos}")
else:
    print(f"Character '{char}' not found")

modified_data = data.replace("!", "?")
print("Modified string:", modified_data)
