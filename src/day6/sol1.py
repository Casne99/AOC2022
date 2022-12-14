from collections import deque


def areAllDifferent(deq, size):
    return len(set(deq)) == size


ans = 0
deq = deque(maxlen=4)
input = open("src/day6/input.txt").read()

for i, char in enumerate(input):
    deq.appendleft(char)
    if areAllDifferent(deq, 4):
        ans = i + 1
        break

print(ans)
