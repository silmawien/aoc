import re

def parse(line):
    args = re.search(r'Sensor at x=(\S*), y=(\S*): closest beacon is at x=(\S*), y=(\S*)', line)
    x, y, bx, by = [int(a) for a in args.groups()]
    dst = abs(bx - x) + abs(by - y)
    return [x, y, dst, bx, by]

with open("input15") as f:
    beacons = [parse(line) for line in f.read().strip().split("\n")]

#s = set()
#row = 2000000
#for b in beacons:
#    dy = abs(b[1] - row)
#    for dx in range(b[2] - dy + 1):
#        s.add(b[0] - dx)
#        s.add(b[0] + dx)
#
#for b in beacons:
#    if b[4] == row:
#        if b[3] in s:
#            s.remove(b[3])
#
#print(len(s))

# part2
candidates = set()
lim = 4000000
#lim = 20
for b in beacons:
    print(b)
    sx, sy, d = b[0:3]
    r = d + 1
    for i in range(r + 1):
        for dx, dy in [[i, r-i], [-i, r-i], [i, -(r-i)], [-i, -(r-i)]]:
            cx = sx + dx
            cy = sy + dy
            if cx >= 0 and cx <= lim and cy >= 0 and cy <= lim:
                candidates.add((sx + dx) * 4000000 + (sy + dy))

print(len(candidates))
for c in candidates:
    x, y = c // 4000000, c % 4000000
    if not any(abs(b[0] - x) + abs(b[1] - y) <= b[2] for b in beacons):
        print(c)
        exit()
