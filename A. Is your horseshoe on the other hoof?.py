n,e,d,r=map(int,input().split())
l=[]
countn=0
counte=0
countd=0
countr=0
t=[]
l.append(n)
l.append(e)
l.append(d)
l.append(r)
for i in range (len(l)):
    if n==l[i]:
        countn+=1
    if e==l[i]:
        counte+=1
    if d==l[i]:
        countd+=1
    if r==l[i]:
        countr+=1
print(countn)
print(counte)
print(countd) 
print(countr)
t.append(l.count(n))
t.append(l.count(e))
t.append(l.count(d))
t.append(l.count(r))
print(t)