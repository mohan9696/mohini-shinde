import requests
payloads ={
    "name":"morpheus",
    "job":"leader"
}
resp=requests.post("https://reqres.in/api/users?page=2",)
print(resp)
print(resp.json())
assert resp.json()['job']=='leader'
#leader=!Leader   ........ to find ascii code is defferent


