def roundd(value):
    if int(value)!=value:
        value=int(value)+1
        return value
    else :
        return int(value)
v,y,x=map(float, input().split(' '))
if int(v)>=1:
    k=int(v)/int(x)
    n=roundd(k)
    j=int(y)/int(x)
    o=roundd(j)
    s=n*o
    print(s)