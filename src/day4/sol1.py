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
    smaller, bigger = sorted((pair[0], pair[1]), key=size)
    lower_big, upper_big = bounds(bigger)
    alreadyChecked = sectionsList(lower_big, upper_big)
    lower_small, upper_small = bounds(smaller)
    if all(elem in alreadyChecked for elem in sectionsList(lower_small, upper_small)):
        ans += 1

print(ans)
