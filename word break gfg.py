n=int(input())
for _ in range(n):
    length=int(input())
    dic=input().split()
    s=input()
    l,fl='',''
    for i in s:
        l+=i
        if l in dic:
            fl+=l
            l=''
    if len(fl)==len(s):
        print(1)
    else:
        print(0)
    
