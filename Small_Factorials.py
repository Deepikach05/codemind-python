t=int(input())
for i in range(t):
    a=int(input())
    p=1
    for i in range(2,a+1):
        p*=i
    print(p)