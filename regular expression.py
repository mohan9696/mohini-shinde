import re
x='[a]?'
match=re.finditer(x,"abcd")
for i in match:
    print(i.start(),i.end(),i)