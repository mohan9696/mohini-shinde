import requests
import json
mydata =open('abc.json','r').read()
print(mydata)
r=requests.post('https://reqres.in/api/users',data=mydata)
print(r)


