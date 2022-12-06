from collections import deque


def areAll4Different(deq):
    if len(deq) == 4:
        return all(deq.count(elem) == 1 for elem in deq)


ans = 0
deq = deque(maxlen=4)
input = open("src/day6/input.txt").read()

for i, char in enumerate(input):
    deq.appendleft(char)
    if areAll4Different(deq):
        ans = i + 1
        break

print(ans)
