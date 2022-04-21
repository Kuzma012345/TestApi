from ast import Assert
import json
import assertions
import requests

from urllib import response
from base_case import BaseCase
from datetime import datetime

from assertions import Assertions

class TestUserRegiester(BaseCase):
    def setup(self):
        randomtime = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"test{randomtime}@test.com"

        self.data = {
            'password':'123',
            'username':'learnqa',
            'firstName':'learnqa',
            'lastName':'learnqa',
            'email': self.email
        }
    
    def testCreateUser(self):
        response = requests.post("https://playground.learnqa.ru/api/user/", data = json.dumps(self.data))

        Assertions.assertJsonKey(response,"id")
        Assertions.assertCodeStatus(response,200)

    def testUserExist(self):
        self.email = 'vinkotov@example.com'

        response = requests.post("https://playground.learnqa.ru/api/user/", data = json.dumps(self.data))

        Assertions.assertCodeStatus(response,400)
        assert response.content.decode("utf-8") == f"Users with email '{self.data['email']}' already exists"