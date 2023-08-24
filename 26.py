#Super MRO Important Example
 
class A:
    def m1 (self):
        print('m1 of A')
class B:
    def m1 (self):
        print('m1 of B')
        
class C(A,B):
    def m2 (self):
        super().m1()
        
c1=C()
c1.m2()
        
