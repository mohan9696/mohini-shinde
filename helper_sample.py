
import requests
from comman_helper import *
import requests
class helper_sample:
    def __init__(self):
        self.comom_obj==helper_sample()

        def get_api(self,url):
            resp=requests.get(url)
            result=self.comom_obj.validate_api(resp)
            print(resp,result)
            if result:
                return resp
            else:
                return result

if __name__== '__main__':
    obj=helper_sample()
    obj.get_api("https://reqres.in/api/users?page=2")




