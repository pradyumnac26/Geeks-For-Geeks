t=int(input())
for i in range(t):
    n=int(input())
    flag=1
    for i in range(1,n):
        val=bin(i)
        if(i+val.count('1')==n):
            flag=0
            break
    print(flag)
