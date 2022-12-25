from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

with open(0) as f:
    raw = [line.strip() for line in f]

h = len(raw)
w = len(raw[0])
start = (raw[0].index("."), 0)
end = (raw[h - 1].index("."), h - 1)
v = defaultdict(list)
for x in range(1, w):
    for y in range(1, h):
        if raw[y][x] in "v^<>":
            v[(x, y)].append(raw[y][x])

dirs = { ">": (1, 0), "<": (-1, 0), "^": (0, -1), "v": (0, 1) }

def step(v):
    v2 = defaultdict(list)
    for p, cs in v.items():
        for c in cs:
            d = dirs[c]
            x = ((p[0] + d[0] - 1) % (w - 2)) + 1
            y = ((p[1] + d[1] - 1) % (h - 2)) + 1
            v2[(x, y)].append(c)
    return v2

def debug(v, s, e):
    for y in range(h):
        for x in range(w):
            if x == 0 or x == w-1 or y == 0 or y == h-1:
                print("#" if (not (s == (x, y) or e == (x, y))) else ".", end='')
            else:
                count = len(v[(x, y)])
                if count > 1:
                    print(count, end='')
                elif count == 1:
                    print(v[(x, y)][0], end='')
                else:
                    print(".", end='')
        print()

#for i in range(10):
#    print(i)
#    debug(v, start, end)
#    v = step(v)

def manhattan(a, b):
    return sum(abs(a1 - b1) for a1, b1 in zip(a, b))

def adj(x, y):
    r = []
    for dx, dy in dirs.values():
        if x + dx > 0 and x + dx < w-1 and y + dy > 0 and y + dy < h-1:
            r.append((x+dx, y+dy))
    if manhattan(start, (x, y)) == 1:
        r.append(start)
    if manhattan(end, (x, y)) == 1:
        r.append(end)
    return r

def search(v, s, e):
    todo = defaultdict(set)
    todo[0].add(s)
    t = 0
    while t < 10000:
        #print("t", t)
        c = 0
        pv = v
        v = step(v)
        for p in todo[t]:
            c += 1
            if p == e:
                return (t, pv)
            if p not in v:
                todo[t+1].add(p)
            for p2 in [a for a in adj(*p)]:
                #d = abs(p2[0] - s[0]) + abs(p2[1] - s[1])
                #if d < t // 2 - 10:
                #    continue # guess too long
                if p2 in v:
                    continue
                todo[t+1].add(p2)
        #print("c", c)
        t += 1

t, vt = search(v, start, end)
print(t)
#print(debug(vt, start, end))
t2, vt2 = search(vt, end, start)
t3, vt3 = search(vt2, start, end)
print(t + t2 + t3)
