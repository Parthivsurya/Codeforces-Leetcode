n=input()
count=1
Flag=0
list1=list(n.split())
for i in range(len(n)-1):
    if n[i]==n[i+1]:
        count=count+1
        if count==7:
            print('YES')
            Flag=1
            break
    else:
        count=1
if Flag==0:
    print('NO')