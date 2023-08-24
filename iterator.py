

import sys



L1= [1,2,3,4,5,6,7,8,9,10,1,11]
n=iter(L1)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(next(n))
for i in L1:
    print(i)







sys.exit(0)
L1= [1,2,3,4,5]
n=iter(L1)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())