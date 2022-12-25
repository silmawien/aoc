with open("input13") as f:
    packet = [list(map(eval, pair.split("\n"))) for pair in f.read().strip().split("\n\n")]

def dbg(f):
    def helper(a, b):
        print(a, b)
        c = f(a, b)
        print("=> {}".format(c))
        return c
    return helper

# -1, 0 or +1 depending on a
#@dbg
def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b
    elif isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            c = cmp(a[i], b[i])
            if c != 0:
                return c
        return len(a) - len(b)
    else:
        if isinstance(a, int):
            return cmp([a], b)
        else:
            return cmp(a, [b])

print(sum(i+1 if cmp(p[0], p[1]) < 0 else 0 for i, p in enumerate(packet)))

# part 2

import functools

flat = [p for ps in packet for p in ps] + [[[2]]] + [[[6]]]
sflat = sorted(flat, key=functools.cmp_to_key(cmp))
from operator import mul
print(functools.reduce(mul, [sflat.index(i)+1 for i in [[[2]], [[6]]]]))
