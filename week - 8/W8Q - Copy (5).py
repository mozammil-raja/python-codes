data = "Python rules!"

# Obtain list of words
words = data.split()
print("List of words:", words)

# Convert to uppercase
upper_data = data.upper()
print("Uppercase:", upper_data)

# Locate position of "rules"
position = data.find("rules")
print("Position of 'rules':", position)

# Search a given character
char = input("Enter a character to search: ")
char_position = data.find(char)
if char_position != -1:
    print(f"Character '{char}' found at position {char_position}")
else:
    print(f"Character '{char}' not found")

# Replace exclamation with question mark
modified_data = data.replace("!", "?")
print("Modified string:", modified_data)
