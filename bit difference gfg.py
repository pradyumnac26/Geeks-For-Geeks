for _ in range(int(input())):
    n1,n2 = list(map(int,input().split()))
    z=bin(n1^n2)
    print(z.count("1"))
