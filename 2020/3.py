from functools import reduce
from math import prod

with open("input_3.txt") as f:
    grid = []
    for line in f.readlines():
        grid.append(list(line)[:-1])

    # part 1

    # count = 0
    # x_pos = 0
    # width = len(grid[0])
    # for row in grid:
    #     if row[x_pos % width] == "#":
    #         count += 1
    #     x_pos += 3
    # print(count)

    counts = [0, 0, 0, 0, 0]
    x_pos = [0, 0, 0, 0, 0]
    y_pos = [0, 0, 0, 0, 0]
    deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    width = len(grid[0])
    height = len(grid)

    for i in range(len(counts)):
        while y_pos[i] < height:
            if grid[y_pos[i]][x_pos[i] % width] == "#":
                counts[i] += 1
            y_pos[i] += deltas[i][1]
            x_pos[i] += deltas[i][0]

    print(prod(counts))
