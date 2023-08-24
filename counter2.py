
import sys
from collections import Counter
str=[1,1,1,2,2,3,8,9,2,1,1]
m=Counter(str)
d=m.most_common()
print(d)
l1=[i[0]+i[1]for i in d]
print(l1)
sys.exit(0) 