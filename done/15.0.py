import sys
# tabulation


# init map
grid = [[0 for i in range(21)] for i in range(21)]
for i in range(0, 20, 1):
    grid[i][20] = 1; grid[20][i] = 1


for i in range(19, -1, -1):
    for j in range(19, -1, -1):
        grid[i][j] = grid[i+1][j] + grid[i][j+1]
    # print(grid[i])
print(grid[0][0])
