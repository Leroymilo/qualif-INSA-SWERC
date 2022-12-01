n, m = map(int, input().split())

C: dict[int, list[list[int]]] = {}
for r in range(n) :
    line = list(map(int, input().split()))
    for c in range(m) :
        color = line[c]
        if color not in C :
            C[color] = [[], []]
        C[color][0].append(r)
        C[color][1].append(c)

s = 0

for coords in C.values() :
    for vals in coords :
        l = len(vals)
        vals.sort()
        cum_vals = [0]
        for i in range(l) :
            cum_vals.append(cum_vals[-1] + vals[i])
        
        for i in range(l) :
            s += vals[i] * i - cum_vals[i]

print(s)