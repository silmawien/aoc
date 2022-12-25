import re

valves = dict()
with open(0) as f:
    for line in f:
        p1, p2 = line.split(";")
        id = re.search(r"Valve (\S+) has flow rate=(\d+)", p1).groups()
        conn = re.findall(r"[A-Z]{2}", p2)
        valves[id[0]] = [int(id[1]), conn]

#print(valves)

# create a dense graph between all useful valves (rate > 0)
useful = [key for key, val in valves.items() if val[0] > 0]

def closest(src, dst):
    visited = set()
    todo = [ [src, []] ]
    while len(todo) > 0:
        cur, path = todo.pop(0)
        if cur == dst:
            return path
        for step in valves[cur][1]:
            if step not in visited:
                visited.add(step)
                todo.append([step, path + [step]])

path = {}
for src in ['AA'] + useful:
    path[src] = {}
    for dst in [n for n in useful if n != src]:
        path[src][dst] = closest(src, dst)

def v(on):
    """The final value of a result"""
    return sum(valves[pos][0] * time for pos, time in on.items())

# slow search with debug info
#def search(on, time, pos):
#    if time <= 0:
#        return on
#    if valves[pos][0] > 0:
#        time -= 1
#        cur = dict(**on, **{pos: time})
#    else:
#        cur = dict(**on)
#    assert(pos not in on)
#    todo = [e for e in useful if e != pos and e not in on]
#    if not todo:
#        return cur
#    return max((search(cur, time - len(path[pos][dst]), dst) for dst in todo), key=v)
#
#a = search({}, 30, 'AA')
#print (30, a, v(a))

indices = {name:i for i, name in enumerate(useful)}
#print(indices)
cache = {}
stats = [0, 0]
def search2(on, time, pos):
    global stats
    stats[0] += 1
    if (on, time, pos) in cache:
        stats[1] += 1
        return cache[(on, time, pos)]
    M = 0
    for u in useful:
        bit = 1 << indices[u]
        if on & bit > 0:
            continue
        dt = len(path[pos][u]) + 1
        if dt >= time:
            continue
        M = max(M, search2(on | bit, time - dt, u) + (time - dt) * valves[u][0])
    cache[(on, time, pos)] = M
    return M

for t in range(1, 31):
    print(t, search2(0, t, 'AA'))

# part 2
# try all 2^n splits of valves between me and my elephant, even though most of them are unlikely
combos = (1 << len(useful)) - 1
for t in range(26, 27):
    me = lambda mask: search2(mask, t, 'AA')
    ele = lambda mask: search2(combos - mask, t, 'AA')
    r = max(((mask, me(mask), ele(mask)) for mask in range(combos)), key=lambda x: x[1] + x[2])
    print(t, r, r[1] + r[2], stats[1] / stats[0], stats[0])
