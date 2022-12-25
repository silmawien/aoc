with open(0) as f:
    d = [int(x) for i, x in enumerate(f.read().strip().split("\n"))]
print(d)
size = len(d)

def mix(d, n):
    for i in range(size):
        start = n.index(i)
        steps = d[i]
        del n[start]
        end = (start + steps) % (size-1)
        if end == 0:
            end = size
        n.insert(end, i)

n = list(range(size))
mix(d, n)
i0 = d.index(0)
n0 = n.index(i0)
print(sum(d[n[(n0 + i) % size]] for i in [1000, 2000, 3000]))
    
dd = [811589153 * v for v in d]
n = list(range(size))

for r in range(10):
    mix(dd, n)
    print(r, [dd[k] for k in n])

i0 = d.index(0)
n0 = n.index(i0)
print(sum(dd[n[(n0 + i) % size]] for i in [1000, 2000, 3000]))
