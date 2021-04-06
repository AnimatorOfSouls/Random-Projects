list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])

pos = 0
maxpos = len(list[0])-1

trees = 0

for row in list:
    if row[pos] == "#":
        trees = trees + 1
    pos = pos + 3
    if pos > maxpos:
        pos = pos - maxpos - 1

print(trees)
