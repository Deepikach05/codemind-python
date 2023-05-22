a=input()
s,p=0,1
for i in a:
    p*=int(i)
    s+=int(i)
print(p-s)