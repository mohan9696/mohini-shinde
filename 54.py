import sys
l1= ["22222","Mohan", ["India","Good", ["Chandrakant","Day"]]]
def f1(nested_list):
    l2 =[]
    for item  in nested_list:
        if isinstance(item,list):
            l2.extend(f1(item))
    
        else:
             l2.append(item)
    return 
        

l2=f1(l1)

sys,exit(0)

#####
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
