import sys
# dublicates output in dictionary format
a=[10,200,3,40,50,12]
b=[]
res={}
for i in a:
    res[i]=a.count(i)
    if i not in b:
        b.append(i)
    else:
        print(i)
print(list(b))
print(res)        


#dublicate words from sentence
s = ["I am very happy"]
word = ' '.join([str(elem) for elem in s])
s
for i in range(0,len(word)):
  count = 1
  for j in range(i+1, len(word)):
     if(word[i]==(word[j])):
       count = count + 1
       word[j] = "0"
     if(count > 1 and word[i] != "0"):
         print(word[i])



sys,exit(0)
a=["Mohan","Shubham","Raju","Sidharaya"]
b=["Shinde","Hiremath","'Bhiradkar","Shegunshi"]
m=zip(a,b)
print(dict(m))

sys,exit(0)

l1= ['a','b','c','d']
l2= [1,2,3,4]
d=zip(l1,l2)
print(dict(d))



sys,exit(0)
a='poiuytrewqaqwertyuio'
print(a[2:13:2])
#o/p= iyrwa

sys ,exit(0)
list1='pune mumbai maharastra india'
print(list1[1:10:2])
# o/p=uemma

sys,exit(0)

#show only duplicates output in list
list=[10,20,30,20,10,40,50,10]
new=[]
for i in list:
    n=list.count(i)
    if n>1:
        if new.count(i)==0:
          new.append(i)
print(new)        

sys,exit(0)

#.7 Bubble sorting
def  Bubble_sort(array):
    n=len(array)
    for i in range(n):
      for j in range(n-i-1):
          if array[j]>array[j+1]:
              array[j],array[j+1]=array[j+1],array[j]
array=[2,3,4,5,6,8,9,7,]

print(array)



sys,exit(0)
#6. print the element of an array:
arr=[1,2,3,4,5,6,7,8,9]
#Loop through the Array bt incrementing the value of i
for i in range(0,len(arr)):
    print(arr[i],end='')


sys,exit(0)
#5. largest number of list:
list=[20,30,40,50,25,10]
list.sort()
print(" the large number:",list[-1])



sys,exit(0)
#4. second largest number of list:
list=[20,30,40,50,25,10]
list.sort()
print(" the second large number:",list[-2])





sys,exit(0)
#3. insertion sort
n=[1,23,33,4,25,65,5,0]
for i in range(len(n)):
    for j in range(+1,len(n)):
        if n[i]<n[j]:
            n[i],n[j]=n[j],n[i]
            print(n)





sys,exit()
#2. find the unique character in given string:
a= 'bbdggjj2345@#T%^&*'
unique_char=[]
for character in a:
    if character not in unique_char:
        unique_char.append(character.lower())
    else:
        unique_char.remove(character.lower())
print(format(unique_char))            





sys,exit(0)

#1. show only duplicates:
a=[1,2,3,4,5,6,4,4,5,5,7,8,9]
b= []
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i,end="")
#print(b)    

sys,exit(0)