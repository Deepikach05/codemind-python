t=int(input())

for i in range(t):

    a=input()

    for j in a:

        if j.isdigit():

            print('Yes')

            break

    else:

        print('No')