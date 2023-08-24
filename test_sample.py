from Helper_sample import *
import pytest
class test_sample:

    def __init__(self):
        self.obj_sample=helper_sample()

    def test_frist_get(self):
        data=self.obj_sample.get_api()
        print(data.content)

if __name__=='__main__':
    obj1=test_sample()
    obj1.test_frist_get()
