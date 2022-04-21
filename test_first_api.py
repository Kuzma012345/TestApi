from urllib import response
import requests
import pytest



class TestFirstAPI:
    names = [
        "danil",
        "Test",
        ""
    ]
    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name': name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong code response"

        response_dict = response.json()

        print(response_dict)

        assert "answer" in response_dict, "No needed key"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

  
        actual_response_text = response_dict["answer"]
        assert expected_response_text == actual_response_text, "Response text does not match"
