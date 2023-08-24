    
    
    
def smart_div(fun):
    def inner (a,b):
        if b==0:
            print('cant divide')
        else:
            return fun (a,b)
    return inner
    
@smart_div
def div_cal(a,b):
        return(a,b)
d=div_cal(10,0) # b==0---->> cannot divide
print(d)            
        