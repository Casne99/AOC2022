import math


class TreeField:

    def __init__(self, xlim, ylim, grid):
        self.xlim = xlim
        self.ylim = ylim
        self.grid = grid.copy()

    def height(self, x, y):
        return self.grid[(x, y)]

    def list_from_to(self, x, y, to):
        if to == "TOP":
            return list(self.height(x, p) for p in range(y, self.ylim + 1))
        if to == "RIGHT":
            return list(self.height(p, y) for p in range(x, self.xlim + 1))
        if to == "LEFT":
            return list(self.height(p, y) for p in range(x, -1, -1))
        if to == "BOTTOM":
            return list(self.height(x, p) for p in range(y, -1, -1))

    def scenic_score(self, x, y):
        lists = (self.list_from_to(x, y, dir)
                 for dir in ["TOP", "LEFT", "RIGHT", "BOTTOM"])
        scores = (visible(p) for p in lists)
        return math.prod(scores)


def initialize_grid(grid):
    res = {}
    for y, line in enumerate(reversed(grid)):
        for x, height in enumerate(line.strip()):
            res[(x, y)] = int(height)
    return res


def visible(treeList):
    res = 0
    start = treeList[0]
    if len(treeList) == 1:
        return 0
    prev = start
    for elem in treeList[1:]:
        if elem >= start:
            return res + 1
        else:
            res += 1
    return res


input = open("src/day8/input.txt").readlines()
puzzle = initialize_grid(input)
x_max = max(x for (x, _) in puzzle.keys())
y_max = max(y for (_, y) in puzzle.keys())
field = TreeField(x_max, y_max, puzzle)
ans = max(field.scenic_score(x, y) for x in range(0, field.xlim + 1)
          for y in range(0, field.ylim + 1))
print(ans)
