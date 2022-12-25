import re

with open(0) as f:
    lines, movestr = f.read().split("\n\n")
    b = lines.split("\n")
    moves = re.findall(r"(\d+)([LR]?)", movestr)


seams = []
for i in range(50):
    seams.append(((49, 100+i, 1), (50+i, 99, 0))) # B0
    seams.append(((100, i, 3), (50+i, 50, 2))) # B2
    seams.append(((49-i, 149, 0), (100+i, 99, 0))) # M01
    seams.append(((149-i, 0, 2), (i, 50, 2))) # M23
    seams.append(((0, 100+i, 3), (199, i, 1))) # T0
    seams.append(((149, 50+i, 1), (150+i, 49, 0))) # T1
    seams.append(((150+i, 0, 2), (0, 50+i, 3))) # T3

def step(p, d):
    r = ((p[0] + d[0]) % h, (p[1] + d[1]) % w)
    while r[1] >= len(b[r[0]]) or b[r[0]][r[1]] == " ":
        r = ((r[0] + d[0]) % h, (r[1] + d[1]) % w)
    return r

#print(step(s, (0, -1)))

#print('\n'.join(b), moves)
w, h = len(b[0]), len(b)
ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
turns = { "L": -1, "R": 1 }

s = (0, b[0].index("."), 0)

for m, t in moves:
    steps = int(m)
    turn = turns[t] if t else 0
    d = ds[s[2]]
    p = s[0:2]
    for i in range(steps):
        p2 = step(p, d)
        #print("candidiate", p2)
        if b[p2[0]][p2[1]] != "#":
            p = p2
        #print("move", p)
    s = (p[0], p[1], (s[2] + turn) % 4)
    #print(m, steps, turn, s)

print(1000 * (s[0]+1) + 4 * (s[1]+1) + s[2])

# part 2
def step2(s):
    for a, b in seams:
        if a == s:
            #print("seam hit", a, b)
            return (b[0], b[1], (b[2] + 2) % 4)
        if b == s:
            #print("seam hit", b, a)
            return (a[0], a[1], (a[2] + 2) % 4)
    d = ds[s[2]]
    return (s[0] + d[0], s[1] + d[1], s[2])

s = (0, b[0].index("."), 0)
for m, t in moves:
    steps = int(m)
    turn = turns[t] if t else 0
    p = s[0:2]
    f = s[2]
    for i in range(steps):
        s2 = step2(s)
        #print("candidiate", s, s2)
        if b[s2[0]][s2[1]] != "#":
            s = s2
        #print("move", p)
    s = (s[0], s[1], (s[2] + turn) % 4)
    #print(m, steps, turn, s)

print(1000 * (s[0]+1) + 4 * (s[1]+1) + s[2])
