for f in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    l=0
    r=sum(arr)
    b=0
    for i in range(n):
        l=l+arr[i]
        if l==r:
            b=1
            break
        else:
            r-=arr[i]
        #print(l,r,arr[i])
    if b==1:
        print(i+1)
    else:
        print(-1)
    
