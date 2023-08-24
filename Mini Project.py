#Bank working Sceniors =ATM
print('welcome to SBI Bank')
p=int(input('enter your 4 digit pin number'))
m=30000
if (p==9168):
    print('1-withdrown your money')
    print('2- check your balance')
    print('3- withdrow fast cash')
    c=int(input('please choose your option'))
if(c==1):
        w=int(input('enter  amount'))
        if (w<m and w% 100==0):
            print('please collect your money;w')
        else:
            print('invalid cash')
elif(c==2):
    print('your balance is;m')
elif(c==3):
    print('1 -> 5000')
    print('2 -> 10000')
    print('3 -> 15000')
    f=int(input('enter your choice'))
if(f==1 and 5000<m):
     print('take cash 5000')
elif(f==2 and 10000<m):
    print('take cash 10000 ')
elif(f==3 and 15000<m):
    print('take cash 15000')
else:
    print('Invalid choice')

