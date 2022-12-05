f = open("input.txt")

pairs = 0

for i in f:
    new_string = i.replace("-", ",")
    s = new_string.split(",")


    if ((int(s[0]) <= int(s[2])) and (int(s[1]) >= int(s[3]))) or ((int(s[0]) >= int(s[2])) and (int(s[1]) <= int(s[3]))):
        pairs += 1

print (pairs)