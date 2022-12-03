from string import ascii_lowercase, ascii_uppercase

ans = 0
values = {}

for (c1, c2) in zip(ascii_lowercase, ascii_uppercase):
    values[c1], values[c2] = ord(c1) - 96, ord(c2) - 38


def inCommon(x, groups):
    for group in groups:
        if not x in group:
            return False
    return True


input = open("day3/input.txt").readlines()
group = []

for (i, line) in enumerate(input):
    group.append(line.strip())
    if (i + 1) % 3 == 0:
        for elem in group:
            for char in elem:
                if inCommon(char, group[1:]):
                    ans += values[char]
                    break
            break
        group.clear()

print(ans)
