list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])

for i in range(len(list)):
    for j in range(len(list)):
        for k in range(len(list)):
            if i != j and i != k and j != k:
                if int(list[i])+int(list[j])+int(list[k])==2020:
                    print(int(list[i])*int(list[j])*int(list[k]))
                    break
