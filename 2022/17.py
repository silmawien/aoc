with open(0) as f:
    jet = f.read().strip()

shapes = [
[
    ['#', '#', '#', '#']
],
[
    ['.', '#', '.'],
    ['#', '#', '#'],
    ['.', '#', '.'],
],
[
    ['.', '.', '#'],
    ['.', '.', '#'],
    ['#', '#', '#'],
],
[
    ['#'],
    ['#'],
    ['#'],
    ['#'],
],
[
    ['#', '#'],
    ['#', '#']
],
]

def offsets(s):
    h = len(s)
    o = set()
    for y, row in enumerate(s):
        for x, e in enumerate(row):
            if e == "#":
                o |= {(x, h - y - 1)}
    return o


blocks = [offsets(s) for s in shapes]

v = set()

for x in range(7):
    v |= {(x, 0)}

def valid(x, y):
    return x >= 0 and x < 7 and (x, y) not in v

import itertools
#bs = iter([blocks[i % 5] for i in range(2020)])
bs = iter([blocks[i % 5] for i in range(2020)])
js = iter(itertools.cycle(jet))
b = None
try:
    while True:
        if not b:
            top = max(v, key=lambda x: x[1])[1]
            b = {(x+2, y+top+4) for (x, y) in next(bs)}
            #print("spawn block", top, b)
        # jet
        dx = -1 if next(js) == "<" else 1
        b2 = {(x+dx, y) for (x, y) in b}
        b = b2 if all(valid(*e) for e in b2) else b
        #print("jet", dx, b)
        # fall
        b2 = {(x, y-1) for (x, y) in b}
        if not all(valid(*e) for e in b2):
            #print("settle")
            v |= b
            b = None
        else:
            #print("fall", b2)
            b = b2
except StopIteration:
    pass

top = max(v, key=lambda x: x[1])[1]
#for y in reversed(range(1, top + 1)):
#    print("{} |".format(y % 10), end='')
#    for x in range(7):
#        print("#" if (x, y) in v else ' ', end='')
#    print("|")
#print("  +-------+")
print(top)
    


