from itertools import permutations as p

a=input()

l=p(a)

for i in l:

    print(''.join(i))