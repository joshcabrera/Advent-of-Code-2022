f = open("input.txt")

# A = Rock
# B = paper
# C = scissors
# X = Rock
# Y = Paper
# Z = Scissors

score = 0

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

for x in f:
    if x[0] == "A":
        if x[2] == "X":
            score += (draw + rock)
        elif x[2] == "Y":
            score += (win + paper)
        else:
            score += (lose + scissors)
    elif x[0] == "B":
        if x[2] == "X":
            score += (lose + rock)
        elif x[2] == "Y":
            score += (draw + paper)
        else:
            score += (win + scissors)
    elif x[0] == "C":
        if x[2] == "X":
            score += (win + rock)
        elif x[2] == "Y":
            score += (lose + paper)
        else:
            score += (draw + scissors)

print(score)