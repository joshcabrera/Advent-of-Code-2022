f = open("input.txt")

# A = Rock
# B = paper
# C = scissors
# X = lose
# Y = draw
# Z = win

score = 0

win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

for x in f:
    if x[0] == "A": #rock
        if x[2] == "X":
            score += (lose + scissors)
        elif x[2] == "Y":
            score += (draw + rock)
        else:
            score += (win + paper)

    elif x[0] == "B": #paper
        if x[2] == "X":
            score += (lose + rock)
        elif x[2] == "Y":
            score += (draw + paper)
        else:
            score += (win + scissors)

    elif x[0] == "C": #scissors
        if x[2] == "X":
            score += (lose + paper)
        elif x[2] == "Y":
            score += (draw + scissors)
        else:
            score += (win + rock)

print(score)