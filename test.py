grid = [[1,3],[2,2]]

n = len(grid)
size = n * n
Count = [0] * (size+1)
for i in range(n):
    for j in range(n):
        Count[grid[i][j]] += 1
        
a, b = -1, -1
for i in Count:
    if i == 2:
        a = i
    elif i == 0:
        b = i
print(a, b)