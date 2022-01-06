from django.test import TestCase
from . import views

# Create your tests here.
class AuthAppTestinng(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.dict_data = {
            "name" : "VishnuKrishnathu",
            "email" : "vishnu.krishnathu1999@gmail.com"
        }

    def testCase1(self):
        response = views.DictToBString(self.dict_data)

        print(response)