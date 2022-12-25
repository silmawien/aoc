def parse(line):
    return [[int(n) for n in p.split(",")] for p in line.split(" -> ")]

with open("input14") as f:
    paths = [parse(line) for line in f.read().strip().split("\n")]

h = max(y for path in paths for x,y in path) + 1
w = max(x for path in paths for x,y in path) * 2
minx = min(x for path in paths for x,y in path)
miny = min(y for path in paths for x,y in path)
print("{}-{} x {}-{}".format(minx, miny, w, h))

scan = [["." for x in range(w+1)] for y in range(h+1)]

for path in paths:
    pairs = zip(path[0:], path[1:])
    for a, b in pairs:
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        if dx:
            sx = dx // abs(dx)
            for x in range(a[0], b[0]+sx, sx):
                scan[a[1]][x] = "#"
        if dy:
            sy = dy // abs(dy)
            for y in range(a[1], b[1]+sy, sy):
                scan[y][a[0]] = "#"

def pour():
    o = None
    while True:
        if not o:
            # spawn new grain
            o = [500, 0]
        x, y = o
        if y < h:
            for dx in [0, -1, 1]:
                if not (x + dx) in range(w + 1):
                    return
                if not (y + 1) in range(h + 1):
                    return
                if scan[y+1][x + dx] == ".":
                    o = [x + dx, y + 1]
                    break
        if [x, y] == o:
            # at rest
            scan[y][x] = "o"
            if o == [500, 0]:
                print("full")
                break;
            o = None

pour()
print("\n".join("".join(line[minx:w//2+1]) for line in scan))
print(sum(p == "o" for line in scan for p in line))
        


