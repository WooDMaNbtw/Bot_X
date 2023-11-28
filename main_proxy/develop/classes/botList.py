from develop.routes import Route


class BotList(Route):

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
