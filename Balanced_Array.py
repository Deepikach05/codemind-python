t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    f=0
    for i in range(n):
        a=sum(l[:i]) #I
        b=sum(l[i+1:]) #r
        if a==b:
            f=1
            break
    if f==1:
        print("YES")
    else: 
        print("NO")