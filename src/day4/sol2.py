def size(section):
    lower, upper = bounds(section)
    return upper - lower + 1


def bounds(section):
    splitted = section.split("-")
    return int(splitted[0]), int(splitted[1])


def sectionsList(lower, upper):
    return [*range(lower, upper + 1)]


ans = 0


input = open("src/day4/input.txt").readlines()
for line in input:
    pair = line.split(",")
    sect1, sect2 = pair[0], pair[1]
    bigger, smaller = (sect1, sect2) if size(
        sect1) > size(sect2) else (sect2, sect1)
    lower_big, upper_big = bounds(bigger)
    alreadyChecked = sectionsList(lower_big, upper_big)
    lower_small, upper_small = bounds(smaller)
    if any(elem in alreadyChecked for elem in sectionsList(lower_small, upper_small)):
        ans += 1

print(ans)
