import sys 
def f1(nested_list):
    l2 =[]
    for item in nested_list:
        if isinstance(item,list):
            l2.extend(f1(item))

        else:
            l2.append(item)
    return l2

l1= ["12345" , "Today" , ["Thursday" , "Good" , ["Great" , "Day"]]]
l2=f1(l1)

sys,exit(0)

a="my name is mohan"
b=list(map(len,a.split()))[-1]
print(b)
