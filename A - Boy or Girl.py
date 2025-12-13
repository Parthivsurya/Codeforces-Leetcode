import os,sys,io 
inp=input()
s=set()
str1="CHAT WITH HER!"
str2="IGNORE HIM!"
for i in inp:
    s.add(i)
    
if len(s)%2==0:
    sys.stdout.write(str1+"\n")
else:
    sys.stdout.write(str2+"\n")