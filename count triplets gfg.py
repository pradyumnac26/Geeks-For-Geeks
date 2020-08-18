for f in range(t):
    n=int(input())
    count=0
    arr=list(map(int,input().split()))
    arr.sort()
    s=set(arr)
    for i in range(n-2):
        for j in range(i+1,n-1):
            if((arr[i]+arr[j]) in s):
                count+=1
    if(count==0):
        print(-1)
    else:
        print(count)
