#class oops examples  

class Company:
    var=100
    def __init__(self):
        Company.address='pune'
    @classmethod
    def Comp_name(cls):
        cls.nmae='infosys'
        Company.othername='Capgemini'
    @staticmethod
    def com_employee():
        Company.employee1='Ram'  
print(Company.__dict__)        
            