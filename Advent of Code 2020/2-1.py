list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])

valid = 0
for row in list:
    ls = row.split(" ")

    minmax = ls[0].split("-")
    min = minmax[0]
    max = minmax[1]

    letter = ls[1][0]
    code = ls[2]

    count = 0

    for i in code:
        if i == letter:
            count = count + 1

    if count>=int(min) and count<=int(max):
        valid = valid + 1

print(valid)
