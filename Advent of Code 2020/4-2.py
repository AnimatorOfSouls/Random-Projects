list = []

input = open("readin.txt","r")
for row in input:
    list.append(row[:-1])

valid = 0
count = 0
cid = False
fvalid = True

hclnums = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
eclvals = ["amb","blu","brn","gry","grn","hzl","oth"]
pidvals = ["0","1","2","3","4","5","6","7","8","9"]

for row in list:
    if row == "":
        if cid == False:
            count += 1
        if count == 8 and fvalid == True:
            valid += 1
        count = 0
        cid = False
    else:
        ls = row.split(" ")
        count += len(ls)

        for data in ls:
            val = data[:3]
            dat = data[4:]
            if val == "cid":
                cid = True
            elif val == "byr":
                if len(dat) != 4 or int(dat) < 1920 or int(dat) > 2002:
                    fvalid = False
            elif val == "iyr":
                if len(dat) != 4 or int(dat) < 2010 or int(dat) > 2020:
                    fvalid = False
            elif val == "eyr":
                if len(dat) != 4 or int(dat) < 2020 or int(dat) > 2030:
                    fvalid = False
            elif val == "hgt":
                if dat[-2:] == "cm":
                    if int(dat[:-2]) < 150 or int(dat[:-2]) > 193:
                        fvalid = False
                elif dat[-2:] == "in":
                    if int(dat[:-2]) < 59 or int(dat[:-2]) > 76:
                        fvalid = False
                else:
                    fvalid = False
            elif val == "hcl":
                if dat[0] == "#" and len(dat[1:]) == 6:
                    for char in dat[1:]:
                        if fvalid == True:
                            found = False
                            for c in hclnums:
                                if char == c:
                                    found = True
                            if found == False:
                                fvalid = False
                else:
                    fvalid = False
            elif val == "ecl":
                found = False
                for col in eclvals:
                    if dat == col:
                        found = True
                if found == False:
                    fvalid = False
            elif val == "pid":
                if len(dat) == 9:
                    for char in dat:
                        if fvalid == True:
                            found = False
                            for c in pidvals:
                                if char == c:
                                    found = True
                            if found == False:
                                fvalid = False
                else:
                    fvalid = False


print(valid)
