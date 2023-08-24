# operator overloading .....

class Employee:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
            
       return self.age + other.age 
a1=Employee(21)
a2=Employee(30)
print(a1+a2)