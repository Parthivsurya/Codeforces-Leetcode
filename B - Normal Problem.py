l1=[]
 
textcase=int(input(""))
for i in range (textcase):
    k=[]
    strr=input("")
    if 'a' in strr.lower():
        k=strr.replace("a","b")
    if 'q' or 'p' in strr:
        string=strr
        string = string.replace('p', 'x')
        string = string.replace('q', 'p')
        string = string.replace('x', 'q')
        k=string
    else:
        k=strr
    newstr=k[::-1]
    l1.append(newstr)
for i in l1:
    print(i)
 