for i in range(int(input())):
    a=input()
    ls=[]
    flag=0
    for i in a:
        if i not in ls:
            ls.append(i)
            
        elif i in ls:
            print(i)
            flag=1
            break
    if flag==0:
        print("-1")
