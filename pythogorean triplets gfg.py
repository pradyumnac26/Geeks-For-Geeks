for f in range(int(input())):
    n=int(input())
    b=[]
    arr=list(map(int,input().split()))
    for i in range(len(arr)):
        b.append((arr[i])**2)
    b.sort()
    flag=0
    for i in range(len(b)):
        for j in range(i+1,len(b)):
            if (b[i]+b[j]) in b:
                flag=1
                break
        if flag==1:
            break
    if flag==1:
        print('Yes')
    else :
        print('No')
