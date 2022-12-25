with open("input6") as f:
    stream = f.read().strip()

import itertools

test = stream 
for i, x in enumerate(zip(test, test[1:], test[2:], test[3:])):
    if all(a != b for a, b in itertools.combinations(x, 2)):
        print("result at i+4 = {}".format(i+4))
        break
        
# part 2
substreams = [stream[offset:] for offset in range(14)]
for i, x in enumerate(zip(*substreams)):
    if all(a != b for a, b in itertools.combinations(x, 2)):
        print("result at i+14 = {}".format(i+14))
        break
