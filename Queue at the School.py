a, b = map(int, input().split())
c = input()
d = list(c)

for _ in range(b):   # simulate b seconds
    i = 0
    while i < a-1:
        if d[i] == 'B' and d[i+1] == 'G':
            d[i], d[i+1] = d[i+1], d[i]  # swap
            i += 2  # move two steps ahead to avoid re-swapping
        else:
            i += 1

print("".join(d))