from collections import deque


def areAll14Different(deq):
    if len(deq) == 14:
        return all(deq.count(elem) == 1 for elem in deq)


ans = 0
deq = deque(maxlen=14)
input = open("src/day6/input.txt").read()

for i, char in enumerate(input):
    deq.appendleft(char)
    if areAll14Different(deq):
        ans = i + 1
        break

print(ans)
