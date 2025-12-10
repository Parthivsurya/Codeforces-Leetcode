num=int(input())
l=[]
for i in range(num):
    data=int(input())
    l.append(data)
count=0
for i in range(len(l)-1):
    if l[i]!=l[i+1]:
        count+=1
print(count+1)