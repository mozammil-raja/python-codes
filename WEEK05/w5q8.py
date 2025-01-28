def reverse_str(str):
    return str[::-1]

str = input("Enter a string: ")
words = str.split(" ")

for i in range(len(words)):
    words[i] = reverse_str(words[i])

str = ' '.join(words)
print(str)