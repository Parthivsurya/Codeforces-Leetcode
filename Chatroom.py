L=["h","e","l","l","o"]
c=input()
d=list(c)

number=0
true=0
for i in range(len(d)):
    if d[i]==L[number]:
        number+=1
        if number==5:
            break

   
if number==5:
    print("YES")
else:
    print("NO")