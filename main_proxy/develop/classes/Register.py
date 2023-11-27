from develop.routes import Route


class Register(Route):

    def set_parameters(self, data):
        return super().set_parameters(data)

    def get_method(self):
        return "POST"

    def get_patch(self, id=""):
        return "/users/register"
