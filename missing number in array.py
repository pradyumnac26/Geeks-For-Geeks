  n= int(input())
    a =list(map(int, input().split()))
    m = len(a)+1
    sum= (m*(m+1))//2
    s=0
    for i in a:
        s=s+i
    mn=sum-s
    print(mn)
    t=t-1        
