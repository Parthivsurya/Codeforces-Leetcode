stack=[]
n="CBACBACBACBACBA"
print(list(n))
noofstacks=0
for i in range(len(n)-1):
    if n[i]>n[i+1]:
        print( n[i], n[i+1])
        print(noofstacks)
        
    elif n[i]<n[i+1]:
        noofstacks+=1
        print("in elif",n[i], n[i+1])
        print(noofstacks)

print(noofstacks+1) 