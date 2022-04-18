from requests import JSONDecodeError, Response


class BaseCase:
    def getCookie(self, response: Response, name):
        assert name in response.cookies, "Отсутствует параметр в куки файле"
        return response.cookies[name]

    def getHeader(self, response: Response, name):
        assert name in response.headers, "Отсутствует нужный хедер"
        return response.headers[name]

    def getJsonValue(self, response: Response, name):
        try:
            cache = response.json()
        except JSONDecodeError:
            assert False, f"Не удалось преобразовать json, текст body запроса {response.text}"

        assert name in cache, "Отсутствует нужный ключ"
        return cache[name]
