list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])

valid = 0
count = 0
cid = False
for row in list:
    if row == "":
        if cid == False:
            count += 1
        if count == 8:
            valid += 1
        count = 0
        cid = False
    else:
        ls = row.split(" ")
        count += len(ls)

        for data in ls:
            if data[:3] == "cid":
                cid = True


print(valid)
