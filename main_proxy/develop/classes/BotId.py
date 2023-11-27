from develop.routes import Route


class BotId(Route):

    def get_method(self):
        return "GET"

    def get_patch(self, id=""):
        return f"/bots/{id}"
