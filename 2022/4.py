with open("input4") as f:
    lines = f.read().strip().split('\n')

def to_range(s):
    l, h = (int(x) for x in s.split("-"))
    return range(l, h + 1)

def parse(l):
    a, b = [to_range(x) for x in l.split(",")]
    print(a, b)
    if any(x in a for x in b):
        return 1
    else:
        return 0

ps = [parse(l) for l in lines]
print(sum(ps))
