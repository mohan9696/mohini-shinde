input=['eat','ate','tea','tab','bat','eat','the']
def listout_same(input):
    output=[]
    while input:
        temp_letter=''.join((sorted(input[0])))
        lst=[]
        for i in input:
            if temp_letter==''.join(sorted(i)):
                lst.append(i)
        for words in lst:
            input.remove(words)
        output.append(lst)
    return output
print(listout_same(input))
