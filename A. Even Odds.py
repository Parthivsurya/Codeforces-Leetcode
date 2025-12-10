l=[]
d=[]
n,e=map(int,input().split())
#1, 3, 5, 7, 9, 2, 4, 6, 8, 10
for i in range (1, n+1):
    if i%2==0:
        l.append(i)
    else:
        d.append(i)
new=d+l
print(new[e-1])