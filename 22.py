#  hybrid inheritance in oops example.
 
  
class A:
    def method1(self):
        print('m1 in A')
class B(A):
    def method2(self):
        print('m2 in B')
class C(A):
    def method3(self):
        print('m3 in C')
class D(B,C):
    def method1(self):
        print('m1 in D')  
d=D()
d.method1()      
               
                
                
                
                
                

        
            