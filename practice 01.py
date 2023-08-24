import sys
def f1(nested_list):
    l2 =[]
    for item in nested_list:
        if isinstance(item,list):
            l2.extend(f1(item))

        else:
            l2.append(item)
        return l2 


sys,exit(0)

lst_in = ["12345" , "Today" , ["Thursday" , "Good" , ["Great" , "Day"] ] ]
output = ['12345', 'Today', 'Thursday', 'Good', 'Great', 'Day']