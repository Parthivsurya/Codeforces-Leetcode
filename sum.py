l=eval(input())
tar=int(input())
sum=0
for i in l:
    sum+=i
    if sum>=tar:
        print([0,l.index(i)])
        break