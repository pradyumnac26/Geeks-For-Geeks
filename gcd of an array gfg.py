import math
t=int(input())
while t:
    n=int(input())
    l = list(map(int,input().strip().split()))
    gc=0
    if(len(l)==1):
        gc=l[0]
    else:
        gc=math.gcd(l[0],l[1])
    for i in range(2,len(l)):
        gc=math.gcd(gc,l[i])
    print(gc)
    t  -=1
