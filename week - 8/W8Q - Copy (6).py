from collections import Counter

string = input("Enter a string: ")
char_count = Counter(string)

print("Character frequency:", dict(char_count))
