moves = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "Y": "PAPER",
    "X": "ROCK",
    "Z": "SCISSORS"
}

points = {
    "PAPER": 2,
    "ROCK": 1,
    "SCISSORS": 3,
    "WIN": 6,
    "LOSE": 0,
    "DRAW": 3
}


def round(moveA, moveB):
    if moveA == "ROCK":
        if moveB == "PAPER":
            return "LOSE"
        if moveB == "SCISSORS":
            return "WIN"
        return "DRAW"
    elif moveA == "PAPER":
        if moveB == "PAPER":
            return "DRAW"
        if moveB == "SCISSORS":
            return "LOSE"
        return "WIN"
    else:
        if moveB == "PAPER":
            return "WIN"
        if moveB == "SCISSORS":
            return "DRAW"
        return "LOSE"


input = open("src/day2/input.txt").readlines()
myPoints = 0

for line in input:
    temp = line.split(" ")
    oth_move, my_move = moves[temp[0]], moves[temp[1].strip()]
    myPoints += points[round(my_move, oth_move)] + points[my_move]

print(myPoints)
