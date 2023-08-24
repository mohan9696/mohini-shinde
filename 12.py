# for loops program 

import sys

n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()
sys,exit(0)

# reverse

import sys
n=5
for i in range (n + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  
    sys,exit(0)