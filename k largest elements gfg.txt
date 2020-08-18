for f in range(int(input())):
    x,k=input().split()
    arr=list(map(int,input().split()))
    arr.sort(reverse=True)
    for i in range(int(k)):
        print(arr[i],end=' ')
    print(" ")
    
