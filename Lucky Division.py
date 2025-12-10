L=[4,7,444,447, 474, 477, 744, 747, 774, 777, 44, 47, 74, 77]
l=int(input())
num=0
digits=list(map(int, str(l) ))
for i in range(len(digits)):
    if digits[i] in L:
        num+=1
if num==len(digits):
    print("YES")
else:
    nu=0
    for i in range(12):
        if l%L[i]==0:
            nu=1
            break
    if nu==1:
        print("YES")
    else:
        print("NO")
