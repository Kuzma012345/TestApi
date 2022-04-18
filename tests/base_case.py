from requests import JSONDecodeError, Response


class BaseCase:
    def getCookie(self, response: Response, name):
        assert name in response.cookies, "Missing required parametr in cookie file"
        return response.cookies[name]

    def getHeader(self, response: Response, name):
        assert name in response.headers, "The required key is missing"
        return response.headers[name]

    def getJsonValue(self, response: Response, name):
        try:
            cache = response.json()
        except JSONDecodeError:
            assert False, f"Could not decode json, body text = {response.text}"

        assert name in cache, "The required key is missing"
        return cache[name]
