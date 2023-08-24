#islower string
#isupper string
#istitel string
#isspace string
#all the example  




import sys 

# isspace string 
s1=''
print(s1.isspace()) #output==false

exit(0),sys
s1='  '
print(s1.isspace()) #output==true

exit(0),sys

# istitle string 
s1="om namah shivay"
print(s1.istitle()) #output==false

exit(0),sys

s1="Om Namah Shivay"
print(s1.istitle()) #output==true

exit(0),sys



#isupper string 
s1="MOHAN"
print(s1.isupper()) #output==true

exit(0),sys
s1="mohan"
print(s1.isupper()) #output==false


# islower string
exit(0),sys
s1="mohan"
print(s1.islower()) #output==true

exit(0),sys
s1="MOHAN"
print(s1.islower()) #output==false
