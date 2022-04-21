from email.header import Header
from urllib import response
import requests


class TestHeader:
    def test_header(self):
        expected_header = {'Server': 'Apache'}
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)

        assert response.headers['Server'] == expected_header[
            'Server'], f'Хедер {response.headers["Server"]} не соответствует ожидаемому хедеру {expected_header["Server"]}'
