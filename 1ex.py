# object level example 

var=100 # variable--->module level (Globle variable)
def f1(): # function--->module level
    var10='pune' #functional level--->(Local veriable)
    print('hi') # functional level
    
class Employee: #module level
    var2= 100    #class level
    def f2(self): #method---> class level
        print('hello')  #method level
        
        