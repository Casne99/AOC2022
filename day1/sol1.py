input = open("day1/input.txt").readlines()
maximum = acc = 0

for (idx, line) in enumerate(input):
    if line == '\n':
        maximum = max(acc, maximum)
        acc = 0
    elif idx == len(input)-1:
        maximum = max(int(line), maximum)
    else:
        acc += int(line)

print(maximum)
