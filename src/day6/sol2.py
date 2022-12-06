from collections import deque


def areAllDifferent(deq, size):
    return len(deq) == size and all(deq.count(elem) == 1 for elem in deq)


ans = 0
deq = deque(maxlen=14)
input = open("src/day6/input.txt").read()

for i, char in enumerate(input):
    deq.appendleft(char)
    if areAllDifferent(deq, 14):
        ans = i + 1
        break

print(ans)
