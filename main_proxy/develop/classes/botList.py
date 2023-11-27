from develop.routes import Route


class BotList(Route):
    def set_response(self, data):
        items = data["result"]
        for item in items:
            item["code"] = "12334"
        super().set_response(items)

    def get_method(self):
        return "GET"

    def get_patch(self, id=""):
        return "/bots"
