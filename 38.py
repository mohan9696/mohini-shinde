#Constructor overriding.

class A:
    def __init__(self):
     print('parent class constructor')
class B(A):
    def __init__(self):
     print('child class constructor')
     
c1=B()
c2=A()     