for f in range(int(input())):
    s,b=input().split()
    q=[]
    s=sorted(s)
    b=sorted(b)
    if(s==b):
        print('YES')
    else :
        print('NO')



////////////////
tcase = int(input())
while(tcase!=0):
    a,b = map(str,input().strip().split(' '))
    if len(a) == len(b):
        for char in a:
            if char not in b:
                print('NO')
                break
        else:
            print('YES')
    else:
        print('NO')
        
    
    tcase-=1
