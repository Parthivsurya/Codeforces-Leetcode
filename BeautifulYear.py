inp=int(input())
newvar=inp
found = 0
while (found==0):
    inp += 1
    digits = [int(d) for d in str(inp)]
    newl = set(digits)
    if len(newl) == 4:
        print(inp)
        break
    