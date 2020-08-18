for f in range(int(input())):
    n=int(input())
    arr=list(input().split())
    if n%2==0:
        x=n-1
    else :
        x=n-2
    for i in range(0,x,2):
        arr[i],arr[i+1]=arr[i+1],arr[i]
    print(*arr)
