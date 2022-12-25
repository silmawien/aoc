with open("input8") as f:
    ts = [[int(c) for c in line] for line in f.read().strip().split("\n")]

h = len(ts)
w = len(ts[0])

visible = [[False for tree in row] for row in ts]

def scan(th, x, y, dx, dy):
    if ts[y][x] > th:
        visible[y][x] = True
        th = ts[y][x]
    if x + dx in range(w) and y + dy in range(h):
        scan(th, x + dx, y + dy, dx, dy)

# scan from top and bottom
for x in range(w):
    scan(-1, x, 0, 0, 1)
    scan(-1, x, h-1, 0, -1)

for y in range(h):
    scan(-1, 0, y, 1, 0)
    scan(-1, w-1, y, -1, 0)

print(sum(sum(1 if x else 0 for x in row) for row in visible))

# part 2 - scan outward and multiply
def scanout(th, x, y, dx, dy):
    if x + dx in range(w) and y + dy in range(h):
        if ts[y+dy][x+dx] < th:
            return 1 + scanout(th, x + dx, y + dy, dx, dy)
        else:
            return 1
    else:
        return 0

def scenic_score(x, y):
    return scanout(ts[y][x], x, y, -1, 0) * scanout(ts[y][x], x, y, 1, 0) * scanout(ts[y][x], x, y, 0, 1) * scanout(ts[y][x], x, y, 0, -1)

print(max(scenic_score(x, y) for x in range(w) for y in range(h)))
