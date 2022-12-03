from sortedcontainers import SortedSet
from string import ascii_lowercase, ascii_uppercase

ans = 0

values = {}


for (c1, c2) in zip(ascii_lowercase, ascii_uppercase):
    values[c1], values[c2] = ord(c1) - 96, ord(c2) - 38


input = open("day3/input.txt").readlines()
common = SortedSet()

for line in input:
    bag1, bag2 = (line[:len(line)//2], line[len(line)//2:].strip())
    for elem in bag1:
        common.add(elem)
    for elem in bag2:
        if elem in common:
            ans += values[elem]
            common.clear()
            break

print(ans)
