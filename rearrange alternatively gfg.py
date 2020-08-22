for i in range(int(input())):
    n=int(input())
    arr=list(input().split())
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    list1=[]
    for i in range(n//2):
        list1.append(arr[n-i-1])
        list1.append(arr[i])
    if(n%2!=0):
        list1.append(arr[n//2])
    for i in range(len(list1)):
        print(list1[i],end=" ")
    print(" ")
        
