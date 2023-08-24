import requests
resp=requests.delete('https://reqres.in/api/Users/2')
#print(resp.json())
print(resp.status_code)