
a=int(input())
b=int(input())
c=int(input())
L=[]
L.append(a+b+c)
L.append(a+b*c)
L.append(a*b*c)
L.append((a+b)*c)
L.append(a*(b+c))
print(max(L))