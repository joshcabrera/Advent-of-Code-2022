f = open("input.txt")

topThree = [0, 0, 0]

calories = 0

for x in f:
    if x !="\n":
        calories += int(x)
    
    if x == "\n":
        if calories > topThree[-1]:
            topThree[-1] = calories
            topThree.sort(reverse=True)
        calories = 0
    

print (topThree)
print (sum(topThree))