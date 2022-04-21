from ast import Not
from urllib import response
import requests
from base_case import BaseCase
from assertions import Assertions

class TestUserGetId(BaseCase):
    def testNotAuth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        
        Assertions.assertJsonValue(response,"username","Vitaliy","Expected value is not Vitaliy")
        assert "email" and "lastName" and "firstName" not in response.json(),"response have keys email, lastname and firstname"
