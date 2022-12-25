with open(0) as f:
    jet = [-1 if x == "<" else 1 for x in f.read().strip()]

print(len(jet))

blocks = [
[
    0b00111100,
    0b00000000,
    0b00000000,
    0b00000000,
],
[
    0b00010000,
    0b00111000,
    0b00010000,
    0b00000000,
],
[
    0b00111000,
    0b00001000,
    0b00001000,
    0b00000000,
],
[
    0b00100000,
    0b00100000,
    0b00100000,
    0b00100000
],
[
    0b00110000,
    0b00110000,
    0b00000000,
    0b00000000,
]
]

rpad = [1, 2, 2, 4, 3]
bheight = [1, 3, 3, 4, 2]

# assume 1024 lines is enough tracking
HEIGHT = 1024

import math

v = [0 for x in range(HEIGHT)]

v[0] = 0b11111110
top = 0
bn = 0
num_blocks = 1000000000000
jlen = len(jet)
stats = {}
jn = 0
bn_add = 0
top_add = 0
while bn + bn_add < num_blocks:
    b = [row for row in blocks[bn % 5]]
    l, r = 2, rpad[bn % 5]
    by = (top + 4) % HEIGHT
    # clear any stale v data
    for i in range(4):
        v[(by + i) % HEIGHT] = 0
    btop = top + 4 + bheight[bn % 5] - 1
    while True:
        # shift
        shift = jet[jn % jlen]
        jn += 1
        edge = 0
        if shift < 0:
            if l > 0 and all((b[i] << 1) & v[(by + i) % HEIGHT] == 0 for i in range(4)):
                l -= 1
                r += 1
                for i in range(4):
                    b[i] = b[i] << 1
        else:
            if r > 0 and all((b[i] >> 1) & v[(by + i) % HEIGHT] == 0 for i in range(4)):
                l += 1
                r -= 1
                for i in range(4):
                    b[i] = b[i] >> 1
        if any(b[i] & v[(by - 1 + i) % HEIGHT] != 0 for i in range(4)):
            # settle
            for i in range(4):
                v[(by + i) % HEIGHT] |= b[i]
            top = max(top, btop)
            bn += 1

            bidx = bn % 5
            lcm = abs(jlen * 5) // math.gcd(jlen, 5)
            key = (bidx % lcm, jn % lcm)
            if jn % lcm == 0:
                print(bn, jn, bn % lcm, jn % lcm)
            if key in stats:
                dt = top - stats[key][1]
                db = bn - stats[key][0]
                #print(bn, key, stats[key], top, db, dt)
                print(key, dt, db)
                if bn > 0:
                    m = (num_blocks - bn) // db
                    if m > 0:
                        top_add = dt * m
                        bn_add = db * m
                        print(m, db, top_add, bn_add)
            stats[key] = (bn, top)
            break
        else:
            # fall
            by = (by - 1) % HEIGHT
            btop -= 1

print(bn, top)
print(bn + bn_add, top + top_add)

