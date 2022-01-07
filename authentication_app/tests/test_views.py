from django.http import request
from django.test import TestCase, RequestFactory, Client
from authentication_app import views
from django.urls import reverse
from django.contrib.auth.models import User
import json

# Create your tests here.
class AuthRegisterTestinng(TestCase):


    @classmethod
    def setUpTestData(cls):
        ##user 1
        cls.user1 = {
            "username" : "TestUser", 
            "email" : "test.user@gmail.com",
            "full_name" : "Test User",
            "password" : "testuser@123"
        }

        ##user 2
        cls.user2 = {
            "username" : "VishnuKrishnathu",
            "email" : "vishnu.krishnathu",
            "full_name" : "Vishnu Krishnathu",
            "password" : "vishnu_krishnathu@8762"
        }

        ##user 3
        cls.user3 = {
            "username" : "TestUser",
            "email" : "vishnu.krishnathu1999@gmail.com",
            "full_name" : "Vishnu Krishnathu",
            "password" : "vishnu_krishnathu@8762"
        }

        ##user 4
        cls.user4 = {
            "username" : "RandomUser", 
            "email" : "random.user@gmail.com",
            "full_name" : "Random User",
            "password" : "testuser@123"
        }

        ##user 5
        cls.user5 = {
            "username" : "BinduGopalkrishnan", 
            "email" : "test.user@gmail.com",
            "full_name" : "Bndu Gopalkrishnan",
            "password" : "bindu@123"
        }


    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()


    def testCase1(self):
        request = self.factory.post(
            reverse('registerUser'),
            self.user1,
            content_type="application/json"
        )
        response = views.registerUser(request)
        self.assertEqual(response.status_code, 200)

    # -----Invalid email test-----
    def testCase2(self):
        request = self.factory.post(
            reverse('registerUser'),
            self.user2,
            content_type= "application/json"
        )

        response = views.registerUser(request)
        self.assertEqual(response.status_code, 400)

    # -----Duplicate username test-----
    def testCase3(self):
        self.client.post(
            reverse('registerUser'),
            self.user1,
            content_type="application/json"
        )
        request = self.factory.post(
            reverse('registerUser'),
            self.user3,
            content_type= "application/json"
        )

        response = views.registerUser(request)
        self.assertEqual(response.status_code, 400)

    # -----Duplicate password test-----
    def testCase4(self):
        request = self.factory.post(
            reverse('registerUser'),
            self.user4,
            content_type= "application/json"
        )

        response = views.registerUser(request)
        self.assertEqual(response.status_code, 200)


    # -----Duplicate email test-----
    def testCase5(self):
        self.client.post(
            reverse("registerUser"),
            self.user1,
            content_type="application/json"
        )
        request = self.factory.post(
            reverse('registerUser'),
            self.user5,
            content_type="application/json"
        )
        response = views.registerUser(request)
        self.assertEqual(response.status_code, 400)