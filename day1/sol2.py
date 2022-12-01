input = open("input.txt").readlines()
acc = 0
candidates = []

for (idx, line) in enumerate(input):
    if line == '\n':
        candidates.append(acc)
        acc = 0
    elif idx == len(input) - 1:
        candidates.append(int(line))
    else:
        acc += int(line)

print(sum(sorted(candidates)[-3:]))
