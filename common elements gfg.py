t=int(input())
for i in range(t):
    n1,n2,n3=map(int,input().split())
    a=set(map(int,input().split()))
    b=set(map(int,input().split()))
    c=set(map(int,input().split()))
    g=a.intersection(b,c)
    g=list(g)
    g.sort()
    if len(g)==0:
        print(-1)
    else:
        print(*g)
