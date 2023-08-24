pattern=Re.compile('xy')
m=pattern.finditer('adsadsdfzxxyxyxyx123xy')

for i in m:
    print(i,start(),i.end(),i.group())