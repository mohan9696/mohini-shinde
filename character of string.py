# character of string 
#isalnum()....>
#(a to z,A TO Z,0 TO 9)Alphanumeric

#islower()'abcdef'
#isupper()'ABCDEF'
#is digit()'123456'
#is title()'Ram, Shyam,Pu  ne'
#isspace() having only spaces
 
import sys


s1='4097'
print(s1.isdigit())# output...>true


sys,exit(0)
s1='                                                                                                                     097'
print(s1.isalnum())# output...>true

sys, exit(0)

s1='Pune097'
print(s1.isalpha())# output...>false

