l1= ['eat','ate','tea','bat','tab','eat','the']
d1= {}
for i in l1:
    word=''.join(sorted(i))
    if word in d1:
        d1[word].append(i)
    else:
        d1[word]= [i]
output =list(d1.values())
print(output)