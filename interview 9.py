import sys
def element(lst,lts):
    if len(lst)==len(set(lst)) or (lts)==len(set(lts)):
        return True
    else:
        return False
l1=[10,20,44,55,80]
l2=[10,2,3,41,22,22,34,]
l3=element(l1,l2)
print(l3)


sys,exit(0)
def element(lst):
    if len(lst)==len(set(lst)):
        return True
    else:
        return False
l=[10,20,25,73,67,78]
l1=element(l)
print(l1)

