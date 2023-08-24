# constructor Overloading:-

class Teacher:
    def add__number(self,a,b):
        self.a=a
        self.b=b
        print(self.a-self.b)   
    def add__number(self,a,b,c,d):
        self.a=a 
        self.b=b 
        self.c=c  
        self.d=d   
        print(self.a-self.b-self.c-self.d)
            
t1=Teacher()
t1.add__number(10,5,1,1)
        