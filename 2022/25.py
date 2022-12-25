with open(0) as f:
    I = [l.strip() for l in f]

sn = { "=": -2, "-": -1, "0": 0, "1": 1, "2": 2 }
def s2d(s):
    d = 0
    v = 1
    for i, c in enumerate(reversed(s)):
        d += v * sn[c]
        v *= 5
    return d

def d2s(d):
    s = ""
    while d > 0:
        r = d % 5
        s += "=-012"[(r+2) % 5]
        d = (d+2) // 5
    return s[::-1]

print(d2s(sum(s2d(s) for s in I)))
#for s in I:
#    print("{:10} {:10} {:10}".format(s, s2d(s), d2s(s2d(s))))

