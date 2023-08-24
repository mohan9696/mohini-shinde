import re
pattern=re.compile('xy')
m=pattern.finditer('axyxyxhxyxxhxyxgyuxyxwxyz')
 
for i in m:
    print(i) 
    
    