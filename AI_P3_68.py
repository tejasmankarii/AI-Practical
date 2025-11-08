import heapq

grid = [
    ["S", ".", ".", ".", "."],
    [".", "X", "X", ".", "."],
    [".", ".", ".", "X", "."],
    [".", "X", ".", ".", "G"],
    [".", ".", ".", ".", "."]
]

rows, cols = len(grid), len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "G":
            goal = (i, j)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

directions = [(1,0), (-1,0), (0,1), (0,-1)]
open_list = []
heapq.heappush(open_list, (manhattan(start, goal), start))
came_from = {start: None}
visited = {start}

found = False
while open_list:
    _, current = heapq.heappop(open_list)
    if current == goal:
        found = True
        break

    for dx, dy in directions:
        nx, ny = current[0] + dx, current[1] + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != "X":
            neighbor = (nx, ny)
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_list, (manhattan(neighbor, goal), neighbor))

path = []
if found:
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

for i, j in path:
    if (i, j) != start and (i, j) != goal:
        grid[i][j] = "*"

print("=== Greedy Best-First Search Pathfinding ===\n")
for row in grid:
    print(" ".join(row))
print("\nPath length:", len(path) if found else 0)
