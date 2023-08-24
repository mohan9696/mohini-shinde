#MRO Super Method 1.

class Employee:
    def __init__(self):
        print('constructor of employee class')
        
class Company(Employee):
    def __init__(self):
        super() .__init__()
        print('constructor of company')
        
c1=Company()