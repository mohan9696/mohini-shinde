l1=[1,3,5,7,8,10]
output=[]

for i in range(l1[0],l1[-1]+1):
    if i not in l1:
        output.append(i)
print(output)
s1="India is my country"
s2=s1.split()
s3=''

for words in s2:
    revers_str=words[::-1]
    s3+=revers_str+' '
print(s3.strip())
