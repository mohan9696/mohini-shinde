from Helper_sample import *

class comman_helper:
    def validate_api(self,resp,exstatus_code=200):
        if int(resp.status_code)!=exstatus_code:
            print('failed')
            return False
        else:
            return True
        def resp_proper(self,url):
            self.my=helper_sample("https://reqres.in/api/users?page=2")
            r=self.my.get_api()
            print(r)

if __name__=='__main__':
    obj=helper_sample()
    obj.get_api("https://reqres.in/api/users?page=2")


