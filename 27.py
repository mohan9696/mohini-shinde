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
        
a1=Teacher()
print(type(a1))
a1.subject()  

      
        
