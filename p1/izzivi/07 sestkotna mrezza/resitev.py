directions = {"n": (1, 0), "ne": (0, 1), "se": (-1, 1),
              "s": (-1, 0), "sw": (0, -1), "nw": (1, -1)}

x, y = 0, 0
for step in open("input.txt").read().strip().split(","):
    dx, dy = directions[step]
    x += dx
    y += dy
print(x + y)
