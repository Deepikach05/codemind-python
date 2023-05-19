h,m=map(int,input().split(':'))
angle=abs(30*h-(11/2)*m)
if angle>180:
    print(360-angle)
else:
    print(angle)