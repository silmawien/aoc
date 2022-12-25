with open("input7") as f:
    stream = f.read().strip().split('\n')

root = { "size": 0 }
cwd = root

bigdirs = []

for line in stream:
    if line[0] == "$":
        argv = line[2:].split(" ")
        if (argv[0] == "cd"):
            cwd = root if argv[1] == "/" else cwd[argv[1]]
    else:
        v = line.split(" ")
        if (v[0] == "dir"):
            cwd[v[1]] = { "size": 0, "..": cwd }
        else:
            # regular file
            size = int(v[0])
            cwd[v[1]] = { "size": size }
            d = cwd
            d["size"] += size
            while ".." in d:
                d = d[".."]
                d["size"] += size

import pprint
pprint.pprint(root)

# find dirs <= 100000
sum = 0
def visit(d, func):
    func(d)
    for k, v in d.items():
        if k != "size" and k != ".." and ".." in v:
            visit(v, func)

def addsum(d):
    global sum
    if d["size"] <= 100000:
        sum += d["size"]

visit(root, addsum)
print(sum)

# find smallest d where size(/) - size(d) < 40000000
ds = []
visit(root, lambda d: ds.append(d))
def order(d):
    smaller = root["size"] - d["size"]
    result = smaller if smaller < 40000000 else 0
    print("candidate", smaller, result)
    return result
print(root["size"])
print(max(ds, key=order)["size"])

