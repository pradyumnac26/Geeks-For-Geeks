for f in range(int(input())):
    z=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr[z-2])
