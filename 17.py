#oops in inner class 
class Outerclass:
    def __init__(self):
        print('constructor of outerclass')
    class innerclass:    
        def __init__(self):
            print('constructor of innerclass')
a1=Outerclass()
b=a1.innerclass()            
            
            