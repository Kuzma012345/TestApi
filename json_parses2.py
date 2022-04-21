import json

from random import randint
from textwrap import indent

str_json = """{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/c421526/v421526527/b2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/c630619/v630619166/3e321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}"""


print(type(str_json))

data = json.loads(str_json)
print(type(data))
# print(data["response"]["items"][0])

for i in data["response"]["items"]:
    del i["id"] # del - удаление ключа из json
    i["likes"] = randint(1000,100000) # добавил новый ключ внутрь json
    i["binary"] = None


print(data["response"]["items"])

out_json = json.dumps(data, indent=2) #indent - кол-во отступов

print(type(out_json))

print(out_json)

with open("my.json", 'w') as file:
    json.dump(data, file, indent=3)

with open("my.json", "r") as file:
    data = json.load(file)

print(data)

