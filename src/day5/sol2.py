def parseInstruction(instruction):
    args = instruction.split()
    num, fr, to = args[1], args[3], args[5]
    return int(num), int(fr) - 1, int(to) - 1


def getAnswer(stackList):
    ans = ""
    for stack in stackList:
        ans += stack[-1]
    return ans


input = open('src/day5/input.txt').read().split('\n\n')
rows = input[0].splitlines()
instructions = input[1].splitlines()
crates = []
stacks = []


for line in rows:
    sameHeightCrates = []
    for i, char in enumerate(line):
        if char.isalpha():
            sameHeightCrates.append(char)
        elif char == " " and i % 4 == 2:
            sameHeightCrates.append(None)
    crates.append(sameHeightCrates)


del(crates[-1])
crates.reverse()
for _ in range(len(crates[0])):
    stacks.append([])

for sameHeightElems in crates:
    for i, elem in enumerate(sameHeightElems):
        if elem is not None:
            stacks[i].append(elem)

for instruction in instructions:
    num, fr, to = parseInstruction(instruction)
    toMove = []
    for _ in range(num):
        toMove.insert(0, stacks[fr].pop())
    stacks[to] = stacks[to] + toMove

print(getAnswer(stacks))
