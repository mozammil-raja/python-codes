def AlphabetCount(wrd):
    UpCount = 0
    LowCount = 0

    for x in wrd:
        if x.isupper():
            UpCount += 1
        if x.islower():
            LowCount += 1
    return UpCount, LowCount


word = input("Enter a string: ")
value=AlphabetCount(word)
print(f"uppercase count = {value[0]}, lowercase count = {value[1]}")