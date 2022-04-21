import requests

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"retard":"yes"})
print(response.text)
print(response.status_code)