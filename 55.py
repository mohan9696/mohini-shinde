l1= ["12345" , "Today" , ["Thursday" , "Good" , ["Great" , "Day"]]]
l2 = []
def fun (l1):
    l2 = []
    for i in l1:
        if  isinstance(i,list):
             l2.extend(fun(i))
        else:
            l2.append(i)
    return l2
l1= ["12345" , "Today" , ["Thursday" , "Good" , ["Great" , "Day"]]]
d=fun(l1)
print(d)