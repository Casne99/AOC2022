from string import ascii_lowercase, ascii_uppercase

ans = 0

values = {}


for (c1, c2) in zip(ascii_lowercase, ascii_uppercase):
    values[c1], values[c2] = ord(c1) - 96, ord(c2) - 38


input = open("day3/input.txt").readlines()

for line in input:
    bag1, bag2 = (line[:len(line)//2], line[len(line)//2:].strip())
    for elem in bag1:
        if elem in bag2:
            ans += values[elem]
            break

print(ans)
