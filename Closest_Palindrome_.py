n=int(input())
for i in range(n-1,0,-1):
    temp,rev=i,0
    while i!=0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if temp==rev:
        a=temp
        break
for i in range(n+1,n*2,+1):
    temp,rev=i,0
    while i!=0:
        rem=i%10
        rev=rev*10+rem
        i=i//10
    if temp==rev:
        b=temp
        break
if  abs(n-a)==abs(n-b):
    print(a,b)
elif n-a>n-b:
    print(a)
else:
    print(b)