a=input()
even=0
for i in a:
    if int(i)%2==0:
        even+=1        
if(even==len(a)):
    print('Even')
elif(even==0):
    print('Odd')
else:
    print('Mixed')