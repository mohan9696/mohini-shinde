# class creation in modelus methods

class Employee:
    name="akshay"
    id= 123
    
    def info(self):
        
        print(self.name,self.id)
        print('emp name is {} emp id is{} '.format(self.name,self.id))
       
obj=Employee()
print(obj.name)        
print(obj.id)  
obj.info()
        
    
        
    