def circularArrayRotation(a, k, queries):
    b=[]
    k=k%len(a)
    a=a[-k:]+a[:-k]
    for i in queries:
        b.append(a[i])
    return b
        
