# print(s3.strip())
#
str1="once upon time in india"
str2="aAEeiIoOuU"
str3=''

for i in str1:
    if i in str2:
        str3+= i.replace(i,"#")
    else:
        str3+=i
print(str3)