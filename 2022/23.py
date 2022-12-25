g = set()
with open(0) as f:
    for y, line in enumerate(f):
        for x, c in enumerate(line):
            if c == "#":
                g.add((x, y))

moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def adj(e):
    return [(e[0] + x, e[1] + y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]

def side(e, move):
    if move[0] == 0:
        return [(e[0] + x, e[1] + move[1]) for x in range(-1, 2)]
    else:
        return [(e[0] + move[0], e[1] + y) for y in range(-1, 2)]

from collections import defaultdict

def step(g, t):
    r = set()
    p = defaultdict(list)
    for e in g:
        if all(o not in g for o in adj(e)):
            r.add(e)
        else:
            moved = False
            for ofs in range(t, t+4):
                move = moves[ofs % 4]
                if all(o not in g for o in side(e, move)):
                    dst = (e[0] + move[0], e[1] + move[1])
                    p[dst].append(e)
                    moved = True
                    break
            if not moved:
                r.add(e)
    for dst, es in p.items():
        if len(es) == 1:
            r.add(dst)
        else:
            for e in es:
                r.add(e)
    return r

def debug(g):
    mx, my = min(x for x, y in g), min(y for x, y in g)
    Mx, My = max(x for x, y in g), max(y for x, y in g)
    return '\n'.join([''.join(["#" if (x, y) in g else "." for x in range(mx, Mx+1)]) for y in range(my, My+1)])

def simulate(g):
    for t in range(10):
        g = step(g, t)
    return g

def simulate2(g):
    og = set()
    t = 0
    while t == 0 or og != g:
        og = g
        g = step(g, t)
        t += 1
        #print(t)
        #print(debug(g))
    return t

def empty(g):
    mx, my = min(x for x, y in g), min(y for x, y in g)
    Mx, My = max(x for x, y in g), max(y for x, y in g)
    return sum(1
            for x in range(mx, Mx+1)
            for y in range(my, My+1)
            if (x, y) not in g)

print(empty(simulate(g)))
print(simulate2(g))
