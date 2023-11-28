from develop.routes import Route


class BotList(Route):
    def set_response(self, data):
        print(data)

        if "result" in data:
            for item in data['result']:
                item["response_code"] = 0

        elif "error" in data:
            data["error"]["response_error_code"] = 1

        return super().set_response(data)

    def success(self, response):
        items = response["result"]
        for item in items:
            item["code"] = "12334"
        return super().success(items)

    def error(self, response):
        response["error"]["error_code"] = 123
        return super().error(response)


    def get_method(self):
        return "GET"

    def get_patch(self, id=""):
        return "/bots"
