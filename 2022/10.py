with open("input10") as f:
    cmds = [l.split(" ") for l in f.read().strip().split("\n")]

clock = 0
x = 1
sumx = 0

def tick():
    global clock
    global x
    global sumx
    clock += 1
    if (clock-20) % 40 == 0:
        sumx += x * clock

for c in cmds:
    if c[0] == "noop":
        tick()
    if (c[0] == "addx"):
        tick()
        tick()
        x += int(c[1])

print(sumx)

# part 2

clock = 0
crt = []
x = 1

def tick():
    global clock
    global x
    global crt
    crt += "#" if abs(x - (clock % 40)) < 2 else "."
    clock += 1

for c in cmds:
    if c[0] == "noop":
        tick()
    if (c[0] == "addx"):
        tick()
        tick()
        x += int(c[1])

for row in range(len(crt) // 40):
    print(''.join(crt[row*40:(row+1)*40]))
