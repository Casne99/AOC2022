from sortedcontainers import SortedSet
from string import ascii_lowercase, ascii_uppercase

ans = 0

values = {}


for (c1, c2) in zip(ascii_lowercase, ascii_uppercase):
    values[c1], values[c2] = ord(c1) - 96, ord(c2) - 38


def common(group):
    ans = SortedSet()
    for line in group:
        for elem in line:
            ans.add(elem)


input = open("day3/input.txt").readlines()
group = []

for i, line in enumerate(input):
    group.append(line)
    if len(group) == 3:


print(ans)
