
f = open("input.txt")

maxCalories = 0
calories = 0

for x in f:
    if x !="\n":
        calories += int(x)
        if calories > maxCalories:
            maxCalories = calories
    else:
        calories = 0

print (maxCalories)
    

