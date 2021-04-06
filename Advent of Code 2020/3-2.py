list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])



maxpos = len(list[0])-1

pos1 = pos2 = pos3 = pos4 = pos5 = 0

tree1 = tree2 = tree3 = tree4 = tree5 = 0

index = 0
for row in list:
    if row[pos1] == "#":
        tree1 += 1
    if row[pos2] == "#":
        tree2 += 1
    if row[pos3] == "#":
        tree3 += 1
    if row[pos4] == "#":
        tree4 += 1

    if index%2 == 0:
        if row[pos5] == "#":
            tree5 += 1
        pos5 += 1

    pos1 += 1
    pos2 += 3
    pos3 += 5
    pos4 += 7

    if pos1 > maxpos:
        pos1 -= (maxpos+1)
    if pos2 > maxpos:
        pos2 -= (maxpos+1)
    if pos3 > maxpos:
        pos3 -= (maxpos+1)
    if pos4 > maxpos:
        pos4 -= (maxpos+1)
    if pos5 > maxpos:
        pos5 -= (maxpos+1)

    index += 1

print(tree1)
print(tree2)
print(tree3)
print(tree4)
print(tree5)

print(tree1*tree2*tree3*tree4*tree5)
