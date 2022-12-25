import operator

monkeys = {}
vals = {}
expr = {}
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
with open(0) as f:
    for line in f.read().strip().split("\n"):
        name, exp = line.split(": ")
        ps = exp.split(" ")
        if len(ps) == 1:
            vals[name] = int(exp)
        else:
            expr[name] = [ps[0], ps[1], ps[2]]

def calc(m, vs):
    if not m in vs:
        vs[m] = ops[expr[m][1]](calc(expr[m][0], vs), calc(expr[m][2], vs))
    return vs[m]

print(calc("root", vals.copy()))

# path from root to humn
def r2h(m):
    if m == "humn":
        return ["!"]
    if m in expr:
        e = expr[m]
        l = r2h(e[0])
        if len(l) > 0:
            return ["<"] + l
        r = r2h(e[2])
        if len(r) > 0:
            return [">"] + r
    return []

# part 2

def iv(op, side, f, v):
    if op == "+":
        return lambda x: f(x - v)
    elif op == "-":
        if side == "<":
            return lambda x: f(x + v)
        else:
            return lambda x: f(-x + v)
    elif op == "*":
        return lambda x: f(x / v)
    elif op == "/":
        if side == "<":
            return lambda x: f(x * v)
        else:
            return lambda x: f(v / x)

def bt(m, path):
    if path[0] == "!":
        return lambda r: r
    elif path[0] == "<":
        v = calc(expr[m][2], vals.copy())
        f = bt(expr[m][0], path[1:])
    else:
        v = calc(expr[m][0], vals.copy())
        f = bt(expr[m][2], path[1:])
    op = expr[m][1]
    if m == "root":
        return f(v)
    return iv(op, path[0], f, v)

print(r2h("root"))
print(bt("root", r2h("root")))
