inp=input()
l = list(map(int, input().split()))
maxindex=0
diff=0
if len(l)>=4:
    for i in range(len(l)-1):
        newsum=l[i]-l[i+1]
    diff= newsum
    print(l)