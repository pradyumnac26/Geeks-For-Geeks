for f in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    arr.sort()
    y=arr[k-1]
    print(y)
