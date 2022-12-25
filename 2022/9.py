moves = []
with open("input9") as f:
    for line in f.read().strip().split("\n"):
        d, c = line.split(" ")
        moves = moves + [d] * int(c)

def simulate(moves, knots):
    R = [[0, 0] for x in range(knots)]
    visited = {}
    for move in moves:
        if move == 'D':
            R[0][1] += 1
        elif move == 'U':
            R[0][1] -= 1
        elif move == 'R':
            R[0][0] += 1
        elif move == 'L':
            R[0][0] -= 1
        for i in range(knots-1):
            H = R[i]
            T = R[i+1]
            manhattan = abs(H[0] - T[0]) + abs(H[1] - T[1])
            delta = 1 if manhattan < 3 else 0
            if abs(H[0] - T[0]) > delta:
                T[0] += (1 if T[0] < H[0] else -1)
            if abs(H[1] - T[1]) > delta:
                T[1] += (1 if T[1] < H[1] else -1)
        visited[str(R[-1])] = True
    return len(visited)

print(simulate(moves, 2))
print(simulate(moves, 10))
        
