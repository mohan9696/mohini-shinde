import unittest
class Test_Company(unittest.testCases):
    @unittest.skipIf(1==1,'it  is true')
    def test_Z(self):
        print(' test method in Z')
