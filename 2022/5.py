with open("input5") as f:
    inp = [part.split("\n") for part in f.read().strip().split("\n\n")]

# inp[0] is stacks
#print(inp[0])
stacks = [[] for x in range(0, len(inp[0][-1]) / 4 + 1)]

for line in reversed(inp[0][0:-1]):
    crates = line[1::4]
    for i, c in enumerate(crates):
        if c != ' ':
            stacks[i].append(c)

# inp[1] is moves
import copy
stacks2 = copy.deepcopy(stacks)

import re
for move in inp[1]:
    c, src, dst = [int(v) for v in re.findall(r'\d+', move)]
    for i in range(0, c):
        stacks[dst-1].append(stacks[src-1].pop())

print(''.join([s[-1] for s in stacks]))

# part 2 - move blockwise
stacks = stacks2
for move in inp[1]:
    c, src, dst = [int(v) for v in re.findall(r'\d+', move)]
    tmp = stacks[src-1][-c:]
    del stacks[src-1][-c:]
    stacks[dst-1] += tmp

#print([''.join(s) for s in stacks])
print(''.join([s[-1] for s in stacks]))
