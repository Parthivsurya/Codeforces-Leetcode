n=(input())
new=""
count=0
countlo=0
for i in range(len(n)):
    if n[0].islower():
        if n[i].isupper():
            count+=1
        if n[i].islower():
            countlo+=1

if count==len(n)-1:
    print(n.capitalize())
elif countlo==len(n) and count==0:
    print(n.upper())
elif count==len(n) and countlo==0:
    print(n.lower())

elif n==n.capitalize():
    print(n)
else:
    for i in range(len(n)):
        if n[i].islower() and count==0:
            new+=n[i].upper()
        else:
            if n[i].isupper() and countlo==0:
                new+=n[i].lower()
    print(new)