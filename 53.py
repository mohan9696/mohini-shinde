# Syntax of Nested If list statement
# if (condition):
#  block of statements
# if (conditions):
#   block of statement
# if (conditons):
#   block of statement
# if (condition):
#   block of statement
#Rest of the code
#
import sys 
l1=["Mohan","Chandrakant", ["Shubham", "Pramod" ,["Shinde"]]]
l2 =[]
def fun (l1):
    l2=[]
    for i in l1:
        if isinstance(i,list):
            l2.extend(fun(i))
        else:
            l2.append(i)
    return  l2
l1= ["Mohan","Chandrakant", ["Shubham", "Pramod" ,["Shinde"]]]  
m=fun(l1)
print(m)





sys,exit(0)
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
