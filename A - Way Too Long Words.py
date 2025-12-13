x=int(input())
output=[]
for i in range(x):
    L=input()
    if len(L)>10:
        x=str(L[0]+str(len(L)-2)+L[-1])
        output.append(x)
    else:
        output.append(L)
for i in output:
    print(i)