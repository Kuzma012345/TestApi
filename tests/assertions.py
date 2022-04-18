from requests import JSONDecodeError, Response
import json

class Assertions:
    @staticmethod
    def assertJsonValue(response: Response, name, expectedValue, errorMsg) -> None:
        try:
            responseJSON = response.json()
        except JSONDecodeError:
            assert False, f"Response is not json, request body {response.text}" 

        assert name in responseJSON, f"response doesn`t have key {name}"
        assert responseJSON[name] == expectedValue, f"{errorMsg}"       
