# constructor Overriding

class A:
    def __init__(self):
        print('Parent class constructor')
class B(A):
    def __init__(self):
        print('Clild class constructor')
        
a1=B()
a1=A()        
        