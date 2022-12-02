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
    "VINTO": 6,
    "PERSO": 0,
    "PAREGGIO": 3
}

against = {
    "PAPER": ["ROCK", "SCISSORS"],
    "ROCK": ["SCISSORS", "PAPER"],
    "SCISSORS": ["PAPER", "ROCK"]
}


def round(mossa_A, mossa_B):
    if mossa_A == "ROCK":
        if mossa_B == "PAPER":
            return "PERSO"
        if mossa_B == "SCISSORS":
            return "VINTO"
        return "PAREGGIO"
    elif mossa_A == "PAPER":
        if mossa_B == "PAPER":
            return "PAREGGIO"
        if mossa_B == "SCISSORS":
            return "PERSO"
        return "VINTO"
    else:
        if mossa_B == "PAPER":
            return "VINTO"
        if mossa_B == "SCISSORS":
            return "PAREGGIO"
        return "PERSO"


def gioca(mossa, codice):
    if codice == "Y":
        return mossa
    elif codice == "X":
        return against[mossa][0]
    else:
        return against[mossa][1]


input = open("day2/input.txt").readlines()
mieiPunti = 0

for line in input:
    temp = line.split(" ")
    oth_move, code = moves[temp[0]], temp[1].strip()
    miaMossa = gioca(oth_move, code)
    mieiPunti += points[round(miaMossa, oth_move)] + points[miaMossa]
    print(miaMossa, oth_move)
    # print(mieiPunti)

print(mieiPunti)
