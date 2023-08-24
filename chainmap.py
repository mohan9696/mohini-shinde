from collections import ChainMap
d1={1:10,2:20}
d2={10:100,20:200}
for i in ChainMap(d1,d2):
    print(i)