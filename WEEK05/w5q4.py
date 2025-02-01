str = input("Enter a sentence: ")
Record = {} #dictionary

for s in str.split():
    if s in Record: Record[s] += 1
    else: Record[s] = 1

print(Record)