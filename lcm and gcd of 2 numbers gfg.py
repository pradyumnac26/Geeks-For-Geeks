import math
for f in range(int(input())):
    x,y=map(int,input().split())
    gc=math.gcd(x,y)
    lcm=(x*y)//gc
    print(lcm,gc)
