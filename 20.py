# oops class variable example-3

class company:
    var=100
    def __init__(self):
        company.address='pune'
        
    @classmethod
    def comp_name (cls):
        cls.name='infosys'
        company. othername ='capgemini'
        
    @staticmethod
    def comp_employees():
        company.employees1 ='Ram'
c1=company()
print(c1.var)
print(company.var)
print(c1.address)
print(company.address)
c1.comp_name()
print(c1.name,c1.othername) 
c1.comp_employees()
print(c1.employees1)