class teacher:
    def subject(self):
        print('this subject data structer')
class student:
    def subject(self):
        print('this subject C++')
class hod:
    def subject(self):
        print('this subject python')
class principle:
    def subject(self):
        print('this is database')
l1=[teacher(),student(),hod(),principle()]
def call_method(a):
         a.subject()
         for i in l1:
            call_method(i)




