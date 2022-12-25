
monkey = {}

def expr(op, arg1, arg2):
    def f(x):
        a1 = x if arg1 == "old" else int(arg1)
        a2 = x if arg2 == "old" else int(arg2)
        return a1 * a2 if op == "*" else a1 + a2
    return f

def parse(x):
    line = [l.strip() for l in x.split("\n")]
    #print(line)
    m = {}
    m["items"] = [int(i) for i in line[1].split(":")[1].split(", ")]
    _, _, _, arg1, op, arg2 = line[2].split(" ")
    m["op"] = expr(op, arg1, arg2)
    divisor = int(line[3].split(" ")[-1])
    dst1, dst2 = [int(l[-1]) for l in line[4:6]]
    m["divisor"] = divisor
    m["dst"] = lambda v: dst1 if v % divisor == 0 else dst2
    m["count"] = 0
    return m

with open("input11") as f:
    monkey = [parse(x) for x in f.read().strip().split("\n\n")]

for r in range(20):
    for i,m in enumerate(monkey):
        while (len(m["items"]) > 0):
            item = m["items"].pop(0)
            item = m["op"](item)
            item = item // 3
            dst = m["dst"](item)
            monkey[dst]["items"].append(item)
            m["count"] += 1

top2 = sorted(monkey, key=lambda x: x["count"])[-2:]
print(top2[0]["count"] * top2[1]["count"])
    
# part 2

with open("input11") as f:
    monkey = [parse(x) for x in f.read().strip().split("\n\n")]

omegadiv = reduce(lambda x, y: x * y, [m["divisor"] for m in monkey])

for r in range(10000):
    print(r)
    for i,m in enumerate(monkey):
        while (len(m["items"]) > 0):
            item = m["items"].pop(0)
            item = m["op"](item)
            item = item % omegadiv
            dst = m["dst"](item)
            monkey[dst]["items"].append(item)
            m["count"] += 1

top2 = sorted(monkey, key=lambda x: x["count"])[-2:]
print(top2[0]["count"] * top2[1]["count"])
