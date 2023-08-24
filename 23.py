# MRO concepts example.

class A:
    def method_name(self):
        print('method inside A')
        
    
class B:
    def method_name(self):
        print('method inside B')
        
    
class C:
    def method_name(self):
        print('method inside C')
        
    
class X(A,B):
    def method_name(self):
        print('method inside X')
        
    
class Y(B,C):
    def method_name(self):
        print('method inside Y')
        
class P(X,Y,C):
    def method_name(self):          
        print('method inside P')
        
obj1=P()  
obj1.method_name()             
        
#MRO OF A,Object    
#MRO OF B,Object          
#MRO OF C,Object        
#MRO OF X,A,B,Object        
#MRO OF Y,B,C,Object        
#MRO OF P,X,A,Y,B,C,Object    
print(A.mro())    # just checking  
print(P.mro())    # just checking  