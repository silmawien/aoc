with open("input12") as f:
    hmap = [[c for c in line] for line in f.read().strip().split("\n")]

print(hmap)

def find(target):
    for y, l in enumerate(hmap):
        for x, c in enumerate(l):
            if c == target:
                return x, y
    raise ValueError("{} not found".format(target))

h = len(hmap)
w = len(hmap[0])

minsteps = [[h*w for c in line] for line in hmap]

import sys
sys.setrecursionlimit(h*w)

def fill(x, y, steps, elevation):
    global debug
    # out of bounds?
    if x not in range(w) or y not in range(h):
        return
    # already got a shorter path?
    if minsteps[y][x] <= steps:
        return
    # too steep?
    if ord(elevation) - ord(hmap[y][x]) > 1:
        return
    minsteps[y][x] = steps
    fill(x+1, y+0, steps+1, hmap[y][x])
    fill(x-1, y+0, steps+1, hmap[y][x])
    fill(x+0, y+1, steps+1, hmap[y][x])
    fill(x+0, y-1, steps+1, hmap[y][x])

end = find("E")
start = find("S")
hmap[end[1]][end[0]] = "z"
hmap[start[1]][start[0]] = "a"
fill(end[0], end[1], 0, "z")
#print(minsteps)
print(minsteps[start[1]][start[0]])

# part 2
candidates = [minsteps[y][x] for x in range(w) for y in range(h) if hmap[y][x] == "a"]
print(min(candidates))
