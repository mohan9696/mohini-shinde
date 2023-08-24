def f2(f1):
    min=f1()
    sub=min+333333333
    print(sub)
    
#@f2
def f1():
    return 888888888
f2(f1) 