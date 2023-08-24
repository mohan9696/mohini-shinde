words=['arura','ford','ferrari','honda','nissan','datsun']
for w in words:
    letters = ['a','f','r','r','e','i','o','h','c','s','u','w','a','n','d']
    status = True
    for ch in w:'jcxluhfflsnc.,,j '
         if ch in letters:
             letters.remove(ch)
             continue
         else:
            status=False
            break
    if status:
         print(w)