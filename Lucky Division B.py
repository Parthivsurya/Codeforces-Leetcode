L=[4,7,444,447, 474, 477, 744, 747, 774, 777, 44, 47, 74, 77]
l=int(input())
num=0
digits=list(map(int, str(l) ))
SEVEN=digits.count(7)
four=digits.count(4)
if SEVEN>four:
    print("7")
elif four>SEVEN:
    print("4")
else :
    if SEVEN==four and not (SEVEN==0 and four==0):
        print("4")
    else:
    
        print("-1")