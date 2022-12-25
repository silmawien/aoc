with open(0) as f:
    lines = f.read().strip().split("\n")
    drops = set([tuple([int(coord) for coord in line.split(",")]) for line in lines])

from collections import defaultdict

def surface(drops):
    s = defaultdict(int)
    for d in drops:
        s[(d[0] + 0.5, d[1], d[2])] += 1
        s[(d[0] - 0.5, d[1], d[2])] += 1
        s[(d[0], d[1] + 0.5, d[2])] += 1
        s[(d[0], d[1] - 0.5, d[2])] += 1
        s[(d[0], d[1], d[2] + 0.5)] += 1
        s[(d[0], d[1], d[2] - 0.5)] += 1
    return s

print(len({k for k, v in surface(drops).items() if v == 1}))

# part 2

inf = 60000
b = [[inf, -inf], [inf, -inf], [inf, -inf]]
for d in drops:
    for c in range(3):
        b[c][0] = min(b[c][0], d[c] - 1)
        b[c][1] = max(b[c][1], d[c] + 2)

cover = {(x, y, z) for x in range(*b[0]) for y in range(*b[1]) for z in range(*b[2])}
inv = cover - drops

def clear(s, p):
    if p in s:
        s.remove(p)
        clear(s, (p[0] + 1, p[1], p[2]))
        clear(s, (p[0] - 1, p[1], p[2]))
        clear(s, (p[0], p[1] + 1, p[2]))
        clear(s, (p[0], p[1] - 1, p[2]))
        clear(s, (p[0], p[1], p[2] + 1))
        clear(s, (p[0], p[1], p[2] - 1))

import sys
sys.setrecursionlimit(len(cover))

clear(inv, (b[0][0], b[1][0], b[2][0]))

filled = drops | inv

print(len({k for k, v in surface(filled).items() if v == 1}))
