f = open("input.txt")

count = 14

t = f.readline()

e = 0 

while e < (len(t)-13):
    test = t[e] + t[e+1] + t[e+2] + t[e+3] + t[e+4] \
        + t[e+5] + t[e+6] + t[e+7] + t[e+8] + t[e+9] \
        + t[e+10] + t[e+11] + t[e+12] + t[e+13]

    myset = set(test)
    if len(myset) == len(test):
        print(count)
        break
    count += 1
    e += 1