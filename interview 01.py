def fun(l1):
    l2= []
    for i in l1:
        if isinstance(i,list):
            l2.extend(fun(i))
        else:
            l2.append(i)
    return l2
l1=["1234","today",["thursday","Good",["Great","day"]]]
d=fun(l1)
print(d)