a,b,c = map(int, input().split())
totalnum=0;
for i in range(1,c+1):
    totalnum+=a*i
if totalnum-b<0:
    print(0)
else:
    print(totalnum-b)
    
    
    