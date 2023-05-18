l=int(input())
a=''.join(input().split())
max=0
for i in range(1,l+1):
    if a.find('1'*i)!=-1:
        max=i
print(max)