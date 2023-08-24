import time
import requests

requests.post('',auth=)
resp=requests.get('https://the-internet.herokuapp.com/basic_auth',auth=('admin','admin'))
print(resp)
print(resp.elapsed.total_seconds())
assert resp.elapsed.total_seconds()>1,'Test case is failed'