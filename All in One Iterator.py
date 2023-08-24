import sys

l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n=iter(l1)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())




sys,exit(0)

class A:
    def __init__(self):
        self.var=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.var<10:
            var=self.var
            self.var=self.var+1
            return var 
        else:
           raise StopIteration
a=A()
for i in a:
    print(i)
      
     



sys,exit(0)
class A:
    def __init__(self):
        self.var=1
    def __iter__(self):
        return self
    def __next__(self):
        var1=self.var
        self.var=self.var+1
        return var1
a=A()
for i in a:
    print(i)    
# output = infinite {1,2,3,4,5,...........,n}

sys,exit(0)
#special example
class A:
    def __init__(self):
       self.var=1
a=A()    
for i in a:
    print(i)
# ooutput= "A" Object is not iterable



sys,exit(0)
# iterator
l1=[1,22,22,3,44,58,875,85,858,58,5687,458,4,54,885488,585,855,77548,57]
n=iter(l1)
print(n.__next__())
print(n.__next__())
print(n.__next__())



sys,exit(0)

#iterator is Parentclass of generator
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n=iter(l1)
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(next(n))
for i in l1:
    print(i)
