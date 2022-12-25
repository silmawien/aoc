with open("input") as f:
    sacks = f.read().strip().split('\n')

def to_prio(c):
    if ord(c) >= ord("A") and ord(c) < ord("a"):
        return ord(c) - ord("A") + 26 + 1
    else:
        return ord(c) - ord("a") + 1

def prio(s):
    middle = len(s) / 2
    a = s[0:middle]
    b = s[middle:]
    return to_prio(next(c for c in a if c in b))

def badge(a, b, c):
    print(a, b, c)
    ba = next(d for d in a if d in b and d in c)
    print(ba)
    return to_prio(ba)

print(to_prio("a"))
print(to_prio("A"))
print(to_prio("C"))

print(sum(prio(s) for s in sacks))

print(sum(badge(*chunk) for chunk in zip(sacks[::3], sacks[1::3], sacks[2::3])))

