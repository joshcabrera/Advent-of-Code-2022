f = open("input.txt")

count = 4

t = f.readline()

e = 0 

while e < (len(t)-13):
    test = t[e] + t[e+1] + t[e+2] + t[e+3]

    myset = set(test)
    if len(myset) == len(test):
        print(count)
        break
    count += 1
    e += 1