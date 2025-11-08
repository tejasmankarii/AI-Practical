import heapq, math

grid = [
    [1, 1, 5],
    [1, "X", 1],
    [1, 1, 1]
]

start = (0, 0)
goal = (2, 2)

rows, cols = len(grid), len(grid[0])

def ok(x, y):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != "X"

def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

g = {start: 0}
f = {start: h(start, goal)}
came = {}
pq = [(f[start], start)]

while pq:
    _, cur = heapq.heappop(pq)
    if cur == goal:
        break
    x, y = cur
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if not ok(nx, ny):
            continue
        w = grid[nx][ny]
        ng = g[cur] + w
        if ng < g.get((nx, ny), math.inf):
            g[(nx, ny)] = ng
            f[(nx, ny)] = ng + h((nx, ny), goal)
            came[(nx, ny)] = cur
            heapq.heappush(pq, (f[(nx, ny)], (nx, ny)))

path = []
cur = goal
while cur in came or cur == start:
    path.append(cur)
    if cur == start:
        break
    cur = came[cur]
path.reverse()

out = [["." for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "X":
            out[i][j] = "X"
for i, j in path:
    out[i][j] = "*"
sx, sy = start
gx, gy = goal
out[sx][sy] = "S"
out[gx][gy] = "G"

for r in out:
    print(" ".join(r))
print("Total cost:", g.get(goal, "No path") if path and path[-1] == goal else "No path")
