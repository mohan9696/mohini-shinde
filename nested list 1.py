import sys
def f1(nested_list):
    l2 =[]
    for item in nested_list:
        if isinstance(item,list):
            l2.extend(f1(item))

        else:
            l2.append(item)
        return l2