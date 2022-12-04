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

against = {
    "PAPER": ["ROCK", "SCISSORS"],
    "ROCK": ["SCISSORS", "PAPER"],
    "SCISSORS": ["PAPER", "ROCK"]
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


def gioca(move, code):
    if code == "Y":
        return move
    elif code == "X":
        return against[move][0]
    else:
        return against[move][1]


input = open("src/day2/input.txt").readlines()
myPoints = 0

for line in input:
    temp = line.split(" ")
    oth_move, code = moves[temp[0]], temp[1].strip()
    myMove = gioca(oth_move, code)
    myPoints += points[round(myMove, oth_move)] + points[myMove]

print(myPoints)
