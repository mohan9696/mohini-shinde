def fact(num):
    if num==0:
        result=1
    else:
        result=num*fact(num-1)
    return result
l1=[1,2,3,4,5]
l2=[]
for i in l1:
    l2.append(fact(i))
print(l2)