x,t=map(int, input().split())
time=240-t
counter=0

for i in range(1,x+1):
    if time>=5*i:
        time-= 5*i
        counter+=1
print(counter)