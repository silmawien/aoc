import re
import itertools

bp = []
with open(0) as f:
    for line in f.read().strip().split("\n"):
        raw = re.findall(r'\d+', line)
        n, o1, o2, o3, c3, o4, b4 = map(int, raw)
        costs = [[o1, 0, 0, 0], [o2, 0, 0, 0], [o3, c3, 0, 0], [o4, 0, b4, 0]]
        bp.append(costs)

def wait(needed, production, t):
    if needed == 0:
        return 0
    if production == 0:
        return t
    return -( needed // -production)

cc = 0
def search(t, c, caps, n, b, cache, best):
    global cc
    cc += 1
    key = tuple([t, *n, *b])
    if key in cache:
        return cache[key]
    # assuming we can produce one geode bot per turn
    if t in best and best[t] > n[3] + t * b[3] + (t * (t-1)) // 2:
        return best[t]
    #print(t, c, n, b)
    M = n[3] + t * b[3]
    for btype in range(4):
        if btype != 3 and b[btype] >= caps[btype]:
            continue
        deficit = [max(0, a - b) for a, b in zip(c[btype], n)]
        #print("deficit", btype, deficit)
        dts = [wait(deficit[i], b[i], t) for i in range(4)]
        #print("dts", dts)
        dt = max(dts) + 1
        #print("dt", dt)
        if dt >= t:
            continue
        if btype != 3 and dt + 1 >= t:
            continue
        n2 = [n[i] - c[btype][i] + dt * b[i] for i in range(4)]
        b2 = b[:]
        b2[btype] += 1
        M = max(M, search(t - dt, c, caps, n2, b2, cache, best))
    cache[key] = M
    best[t] = M
    return M

def caps(bp):
    return [max(vs) for vs in zip(*bp)]

tot = 0
for i, c in enumerate(bp):
    print(i, c)
    tot += (i+1) * search(24, c, caps(c), [0, 0, 0, 0], [1, 0, 0, 0], {}, {})
print(tot)
print(cc)

import time
st = time.time()
for t in range(32, 33):
    prod = 1
    for i, c in enumerate(bp[0:3]):
        prod = prod * search(t, c, caps(c), [0, 0, 0, 0], [1, 0, 0, 0], {}, {})
    print(t, prod)
    ot = st
    st = time.time()
    print(st - ot)
print(cc)
