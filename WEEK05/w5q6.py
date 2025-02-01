with open("test.txt", "r") as file:
    tempRec = []
    for line in file:
        tempRec.append(line.lstrip())
    

with open("changed.txt", "w") as file:
    for line in tempRec:
        file.write(line)
