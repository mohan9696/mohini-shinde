# polymorphism  in first example.

class Teacher:
    def subject(self):
        print('this subjectn is Data structure')
        
class Student:
    def subject(self):
        print('this subjectn is C++')
        
class HOD:
    def subject(self):
        print('this subjectn is Python')
        
class Principle:
    def subject(self):
        print('this subjectn is Java')
        
def call_method(x):
    x.subject()
l1=[Teacher(),Student()]   

for i in l1:
    print(i)
     
        
      
        
