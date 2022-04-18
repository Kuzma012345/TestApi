import requests
import pytest

from base_case import BaseCase
from urllib import response
from assertions import Assertions

class TestUserAuth(BaseCase):

    exclude_params = [
        "no_cookie",
        "no_token"
    ]

    def setup(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        self.url = "https://playground.learnqa.ru/api/user/login"
        self.url2 = "https://playground.learnqa.ru/api/user/auth"
        response1 = requests.post(self.url, data=data)

        self.auth_sid = self.getCookie(response1,"auth_sid")
        self.token = self.getHeader(response1,"x-csrf-token")
        self.user_id = self.getJsonValue(response1,"user_id")

    def testAuthUser(self):

        response2 = requests.get(
            self.url2,
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assertJsonValue(response2, "user_id", self.user_id, "Id пользователя не совпадает с id ответ")


    @pytest.mark.parametrize('condition', exclude_params)
    def testNegativeAuth(self, condition):

        # NO COOKIE TOKEN NEGATIVE TEST
        if condition == "no_cookie":
            response2 = requests.get(
                self.url2,
                headers={"x-csrf-token": self.token},
            )

        # NO X-CSRF TOKEN NEGATIVE TEST
        else:
            response2 = requests.get(
                self.url2,
                cookies={"auth_sid": self.auth_sid}
            )
        
        Assertions.assertJsonValue(response2,"user_id", 0, "Статус авторизации пользователя не равен 0")

