mosse = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "Y": "PAPER",
    "X": "ROCK",
    "Z": "SCISSORS"
}

punti = {
    "PAPER": 2,
    "ROCK": 1,
    "SCISSORS": 3,
    "VINTO": 6,
    "PERSO": 0,
    "PAREGGIO": 3
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


input = open("day2/input.txt").readlines()
mieiPunti = 0

for line in input:
    temp = line.split(" ")
    oth_move, my_move = mosse[temp[0]], mosse[temp[1].strip()]
    mieiPunti += punti[round(my_move, oth_move)] + punti[my_move]

print(mieiPunti)
