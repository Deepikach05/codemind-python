a=int(input())
b=str(a*a)
sum=0
for i in b:
    sum+=int(i)
if(sum==a):
    print("Neon Number")
else:
    print('Not Neon Number')