input = open("input.txt").readlines()
acc = 0
top3 = []

for (idx, line) in enumerate(input):
    if line == '\n':
        top3.append(acc)
        acc = 0
    elif idx == len(input) - 1:
        top3.append(int(line))
    else:
        acc += int(line)

print(sum(sorted(top3)[-3:]))
