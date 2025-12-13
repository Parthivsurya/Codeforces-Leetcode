x=int(input())
c=0
for i in range(x):
    x=input("")
    y=str(x).count('1')
    if y >=2:
        c=c+1
print(c)