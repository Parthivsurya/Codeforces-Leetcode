a,b=map(int,input(" ").split())
 
count=0
if a ==b:
    count=count+1
while a<b:
    count=count+1
    a=a*3
    b=b*2
    if a ==b:
        count=count+1
 
print(count)