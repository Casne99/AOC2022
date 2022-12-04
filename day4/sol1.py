from sortedcontainers import SortedSet


def size(section):
    lower, upper = bounds(section)
    return upper - lower + 1


def updateChecked(lower, upper, checkedSet):
    for i in range(lower, upper + 1):
        checkedSet.add(i)


def bounds(section):
    splitted = section.split("-")
    return int(splitted[0]), int(splitted[1])


def isContainedIn(section, alreadyChecked):
    lower, upper = bounds(section)
    for i in range(lower, upper + 1):
        if not i in alreadyChecked:
            return False
    return True


assigned = SortedSet()
ans = 0


input = open("day4/input.txt").readlines()
for line in input:
    pair = line.split(",")
    sect1, sect2 = pair[0], pair[1]
    bigger, smaller = (sect1, sect2) if (
        size(sect1) > size(sect2)) else (sect2, sect1)
    lower, upper = bounds(bigger)
    updateChecked(lower, upper, assigned)
    if isContainedIn(smaller, assigned):
        ans += 1
    assigned.clear()

print(ans)
