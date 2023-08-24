# oops in inheritance program.

class company:
    def m1(self):
        print('1st method')
    def m2(self):
        print('2sd method')
    def m3(self):
        print('3rd method')
    def m4(self):
        print('4rt method')
class Employee(company):        
    def m5(self):
        print('5th method')
b=Employee()
b.m1()
b.m2()
b.m3()
b.m4()
b.m5()
