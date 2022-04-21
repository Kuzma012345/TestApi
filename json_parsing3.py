import requests
import json

response = requests.get("https://petstore.swagger.io/v2/pet/findByStatus?status=available")

pretty_response = json.dumps(response.json(), indent=4)
print(type(pretty_response))
print(type(response.json()))