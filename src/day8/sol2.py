import math


class TreeField:

    def __init__(self, xlim, ylim, grid):
        self.xlim = xlim
        self.ylim = ylim
        self.grid = grid.copy()

    def height(self, x, y):
        return self.grid[(x, y)]

    def is_on_border(self, x, y):
        return x == 0 or y == 0 or x == self.xlim or y == self.ylim

    def is_visible_from(self, cx, cy, pos):
        height = self.grid[(cx, cy)]
        if pos == "TOP":
            return all(self.grid[(cx, y)] < height for y in range(cy + 1, self.ylim + 1))
        elif pos == "BOTTOM":
            return all(self.grid[(cx, y)] < height for y in range(0, cy))
        elif pos == "RIGHT":
            return all(self.grid[(x, cy)] < height for x in range(cx + 1, self.xlim + 1))
        elif pos == "LEFT":
            return all(self.grid[(x, cy)] < height for x in range(0, cx))

    def is_visible(self, x, y):
        return self.is_on_border(x, y) or any(self.is_visible_from(x, y, pos) for pos in ["TOP", "BOTTOM", "RIGHT", "LEFT"])

    def count_visible(self):
        return sum(1 for (x, y) in self.grid.keys() if self.is_visible(x, y))

    def visible_trees(self, x, y, to):
        ty = res = 0
        if to == "TOP":
            while ty < self.ylim + 1:

        return 0

    def scenic_score(self, x, y):
        scores = []

        return math.prod(scores)

    def __str__(self):
        return str(self.grid)


def initialize_grid(grid):
    res = {}
    for x, line in enumerate(reversed(grid)):
        for y, height in enumerate(line.strip()):
            res[(x, y)] = int(height)
    return res


input = open("src/day8/input.txt").readlines()
puzzle = initialize_grid(input)
x_max = max(x for (x, _) in puzzle.keys())
y_max = max(y for (_, y) in puzzle.keys())
field = TreeField(x_max, y_max, puzzle)
ans = field.count_visible()
print(ans)
