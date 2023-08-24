import sys
class Collage:
    var='"pune"'
    def __init__(self):
        self.var=100
    def method1(self):
        print("instance method")
@classmethod
def method2(cls):
    print('class method')
@staticmethod
def methodn3():
    print('''print static method''')
    















sys.exit(0)
class D:
    pass 
class E:
    pass 
class F:
    pass 
class B(D,E):
    pass 
class C(D,F):
    pass 
class A(B,C):
    pass 
print(A.mro())


sys.exit(0)
class Company:
    def m1(self):
        print('inside m1')
C=Company()
C.m1()


        
        
    
  
  
        