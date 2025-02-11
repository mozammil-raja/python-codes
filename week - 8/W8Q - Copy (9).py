def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

def is_palindrome(string):
    return string == string[::-1]

sentence = input("Enter a sentence: ")
print("Reversed words:", reverse_words(sentence))

if is_palindrome(sentence.replace(" ", "").lower()):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
