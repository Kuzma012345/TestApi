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

    @staticmethod
    def assertJsonKey(response: Response, key) -> None:
        try:
            responseJSON = response.json()
        except JSONDecodeError:
            assert False, f"Response is not json, request body {response.text}"

        assert key in responseJSON, f"Missing {key} in JSON"

    @staticmethod                   
    def assertCodeStatus(response: Response, Code) -> None:
        assert response.status_code == Code,\
             f"Unexpected statusCode = {response.status_code}"
