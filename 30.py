# Operator Overloading ex-2

class Employee:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        return self.age + other.age    
    def __sub__(self,other):
        return self.age - other.age    
    def __mul__(self,other):
        return self.age * other.age
    
a1=Employee(21)       
a2=Employee(30)       
a3=Employee(4)
print(a1+a2)    
print(a1-a2)    
print(a1*a2)    
    