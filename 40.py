# import copy

import copy

l1=[1,10,20,3,5,6,7]
l2=copy.copy(l1)
l1[1]='pune'
l2[3]='step'
print(l1,l2)
print(id(l1),id(l2))
