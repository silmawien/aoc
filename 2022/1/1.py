with open("input") as f:
    packs = f.read().strip().split('\n\n')

def packsum(p):
    vs = p.split("\n")
    return sum([int(v) for v in vs])

print(packs)
ps = sorted([packsum(p) for p in packs])
print(sum(ps[-3:]))
